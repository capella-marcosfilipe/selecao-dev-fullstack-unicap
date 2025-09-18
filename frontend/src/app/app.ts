import { Component, OnInit, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AnalysisService } from './services/analysis.service';
import { AnalysisRequest, AnalysisResponse } from './models/analysis.model';
import { finalize } from 'rxjs';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

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
  // ---------------------

  constructor(private analysisService: AnalysisService) {}

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
        },
        error: (err) => {
        // On error, set the error message
          console.log('API error:', err);
          this.error.set('An error occurred while processing your request. Check the console for more details.');
        }
      });
  }

}
