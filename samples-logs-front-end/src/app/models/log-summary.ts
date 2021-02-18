export interface LogSummary {
  import: JobStatusCounts;
  pipeline: JobStatusCounts;
  export: JobStatusCounts;
}

export interface JobStatusCounts {
  Success?: number;
  Processing?: number;
  Failed?: number;
  Undefined?: number;
}
