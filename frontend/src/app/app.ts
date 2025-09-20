import { Component, OnInit, signal } from '@angular/core';
import { AnalysisService } from './services/analysis.service';
import { AnalysisRequest, AnalysisResponse } from './models/analysis.model';
import { finalize } from 'rxjs';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser'

@Component({
  selector: 'app-root',
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  // --- State signals ---
  protected inputText = signal<string>('');
  protected analysisResult = signal<AnalysisResponse | null>(null);
  protected isLoading = signal<boolean>(false);
  protected error = signal<string | null>(null);
  protected highlightedHtml = signal<SafeHtml | null>(null);
  // ---------------------

  constructor(
    private analysisService: AnalysisService, 
    private sanitizer: DomSanitizer
  ) {}

  protected submitAnalysis(): void {
    /**
     * Handles the submission of the analysis request.
     */

    // Prepare the request data
    const requestData: AnalysisRequest = {
      task: 'ner',
      input_text: this.inputText(),
    }

    // Set loading state
    this.isLoading.set(true);
    this.error.set(null);
    this.analysisResult.set(null);

    // Call the analysis service
    this.analysisService.analyze(requestData)
      .pipe( finalize(() => this.isLoading.set(false)) )
      .subscribe({
        // On success, set the analysis result
        next: (response) => {
          this.analysisResult.set(response);

          // Highlight the text
          if (response.result?.['entities']) {
            const htmlString = this.generateHighlightedHtml(this.inputText(), response.result['entities']);
    
            const safeHtml = this.sanitizer.bypassSecurityTrustHtml(htmlString);
            this.highlightedHtml.set(safeHtml);
          }
        },
        error: (err) => {
        // On error, set the error message
          console.log('API error:', err);
          this.error.set('An error occurred while processing your request. Check the console for more details.');
        }
      });
  }

  private generateHighlightedHtml(text: string, entities: any[]): string {
    /**
     * Generates an HTML string with named entities highlighted.
     * This method iterates through the original text and a list of entities,
     * wrapping each entity in a <span> tag with appropriate classes for styling.
     *
     * @param text The original input text.
     * @param entities An array of entity objects, each with a `text` and `label` property.
     * @returns An HTML string with the entities highlighted.
     */

    // If there's no text or no entities, return the original text.
    if (!text || !entities || entities.length === 0) {
      return text
    }

    // Sort entities by their starting position in the text to process them in order.
    const sortedEntities = entities.sort((a, b) => text.indexOf(a.text) - text.indexOf(b.text));

    let lastIndex = 0;
    const parts = [];

    // Iterate through each entity to build the highlighted HTML.
    sortedEntities.forEach(entity => {
      // Find the starting index of the current entity in the text.
      const startIndex = text.indexOf(entity.text, lastIndex);

      if (startIndex !== -1) {
        // Add the text segment before the current entity.
        parts.push(text.substring(lastIndex, startIndex));

        // Create the highlighted HTML for the entity.
        const highlightedPart =
          `<span class="entity-highlight ${entity.label.toLowerCase()}" data-label="${entity.label}">${entity.text}</span>`;
        parts.push(highlightedPart);

        // Update the last index to the end of the current entity.
        lastIndex = startIndex + entity.text.length;
      }
    });

    // Add the remaining text after the last entity.
    parts.push(text.substring(lastIndex));

    // Join all parts to form the final HTML string.
    return parts.join('');
  }

}
