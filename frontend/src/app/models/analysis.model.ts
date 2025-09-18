export interface AnalysisRequest {
    task: string;
    input_text?: string;
    use_external: boolean;
    options: { [key: string]: any };
}

export interface AnalysisResponse {
    id: string;
    task: string;
    engine: string;
    result: { [key: string]: any };
    elapsed_ms: number;
    received_at: string;
}
