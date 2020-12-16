import { summaryFileName } from '@angular/compiler/src/aot/util';
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-filter-pane',
  templateUrl: './filter-pane.component.html',
})
export class FilterPaneComponent implements OnInit {

  constructor() { }

  @Input() public summary;

  public getImport() {
    return this.summary.import;
  }

  ngOnInit() {
  }

}
