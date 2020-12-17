import { Component, OnInit, Input } from '@angular/core';
import { SampleLog } from '@models/sample-log';

@Component({
  selector: 'app-sample-table',
  templateUrl: './sample-table.component.html',
  styleUrls: ['./sample-table.component.css']
})
export class SampleTableComponent implements OnInit {

  @Input()
  data: SampleLog[];

  constructor() { }

  ngOnInit() {
  }

}
