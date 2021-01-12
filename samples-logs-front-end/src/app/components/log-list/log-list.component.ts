import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-log-list',
  templateUrl: './log-list.component.html',
  styleUrls: ['./log-list.component.css']
})
export class LogListComponent implements OnInit {
  @Input() title = 'Logs';
  @Input() logs = [];
  @Input() dates = [];
  @Input() styling: 'success'|'danger';

  constructor() { }

  ngOnInit() {
  }

}
