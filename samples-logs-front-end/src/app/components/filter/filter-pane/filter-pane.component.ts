import { Component, Input, OnInit } from '@angular/core';
import { LogSummary } from '@models/log-summary';
import RunStage from '@models/run-stage';

@Component({
  selector: 'app-filter-pane',
  templateUrl: './filter-pane.component.html',
})
export class FilterPaneComponent implements OnInit {

  constructor() { }

  @Input() public summary: LogSummary;
  @Input() public stage: RunStage;

  public getImport() {
    return this.summary.import;
  }

  ngOnInit() {
  }

}
