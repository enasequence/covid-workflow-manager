import { Component, OnInit } from '@angular/core';
import {Title} from "@angular/platform-browser";
import {ApiDataService} from "../api-data.service";

@Component({
  selector: 'app-samples',
  templateUrl: './samples.component.html',
  styleUrls: ['./samples.component.css']
})
export class SamplesComponent implements OnInit {
  p: number = 1;
  data: any;

  constructor(private title: Title, private dataService: ApiDataService) { }

  ngOnInit() {
    this.title.setTitle('Samples Logs');
    this.dataService.getAllSamples().subscribe(
      data => {
        this.data = data['results'];
      },
      error => {
        console.log(error);
      }
    );
  }

  getDate(item: any) {
    return item.split('-')[0];
  }

  getExportStatus(item: any) {
    return item.indexOf('download finished') !== -1 ? 'Success' : 'Failed';
  }

  getExportStatusClass(item: any) {
    return item.indexOf('download finished') !== -1 ? 'badge badge-pill badge-success' : 'badge badge-pill badge-danger';
  }

}
