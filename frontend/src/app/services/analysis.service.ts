import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AnalysisRequest, AnalysisResponse } from '../models/analysis.model';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AnalysisService {
  private apiUrl = environment.apiHost + '/api/v1/analyze';

  constructor(private http: HttpClient) {}

  analyze(requestData: AnalysisRequest): Observable<AnalysisResponse> {
    const analysis_response = this.http.post<AnalysisResponse>(this.apiUrl, requestData);
    return analysis_response;
  }
}
