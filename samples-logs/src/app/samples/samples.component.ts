import { Component, OnInit } from '@angular/core';
import {Title} from "@angular/platform-browser";

@Component({
  selector: 'app-samples',
  templateUrl: './samples.component.html',
  styleUrls: ['./samples.component.css']
})
export class SamplesComponent implements OnInit {
  p: number = 1;
  data: any[];

  constructor(private title: Title) { }

  ngOnInit() {
    this.title.setTitle('Samples Logs');
  }

}
