import { summaryFileName } from '@angular/compiler/src/aot/util';
import { Component, Input, OnInit } from '@angular/core';

import { get } from 'lodash/fp';

@Component({
  selector: 'app-status-summaries',
  templateUrl: './status-summaries.component.html',
})
export class StatusSummariesComponent implements OnInit {

  @Input() public stage;
  @Input() public summary;

  public getStatuses(stage) {
    return get(stage)(this.summary);
  }

  constructor() { }

  ngOnInit() {
  }

}
