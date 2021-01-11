import { Component, OnInit, Input } from '@angular/core';
import { SampleLog } from '@models/sample-log';

@Component({
  selector: 'app-sample-table',
  templateUrl: './sample-table.component.html',
  styleUrls: ['./sample-table.component.css']
})
export class SampleTableComponent implements OnInit {

  @Input() pipeline: string;
  @Input() data: SampleLog[];
  @Input() filters;
  page = 1;

  sampleCount() {
    return this.data ? this.data.length : 0;
  }

  constructor() { }

  ngOnInit() {
  }

}
