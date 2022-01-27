import { Component, Input, OnInit } from '@angular/core';
import { LogSummary } from '@models/log-summary';
import RunStage from '@models/run-stage';

@Component({
  selector: 'app-status-filter',
  templateUrl: './status-filter.component.html',
})
export class StatusFilterComponent implements OnInit {

  @Input() public stage: RunStage;
  @Input() public summary: LogSummary;

  getStatusCount(stage): number {
    return this.summary[stage] || 0;
  }

  shortName(stage: RunStage): string {
    const xref = {
      import_from_ena: 'import',
      pipeline_analysis: 'pipeline',
      export_to_ena: 'export'
    };
    return xref[stage];
  }

  constructor() { }

  ngOnInit() {
  }

}
