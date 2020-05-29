import { Component, OnInit } from '@angular/core';
import {Title} from '@angular/platform-browser';
import {ApiDataService} from '../api-data.service';

@Component({
  selector: 'app-ont-samples',
  templateUrl: './ont-samples.component.html',
  styleUrls: ['./ont-samples.component.css']
})
export class OntSamplesComponent implements OnInit {
  p = 1;
  data: any;
  statuses = {
    ena_import: {
      success: 'download finished',
      failed: 'download failed'
    },
    pipeline_analysis: {
      success: 'pipeline_finished',
      started: 'pipeline_started'
    },
    ena_export: {
      success: 'submission to ENA finished',
      failed: 'submission to ENA failed'
    }
  };

  constructor(private title: Title, private dataService: ApiDataService) { }

  ngOnInit() {
    this.title.setTitle('ONT Samples Logs');
    this.dataService.getAllSamplesONT().subscribe(
      data => {
        this.data = data.results;
      },
      error => {
        console.log(error);
      }
    );
  }

  getDate(item: any) {
    return item.split('-')[0];
  }

  getExportStatus(item: any, statusType: string) {
    if (item.indexOf(this.statuses[statusType].success) !== -1) {
      return 'Success';
    } else if (item.indexOf(this.statuses[statusType].started) !== -1) {
      return 'Processing';
    } else {
      return 'Undefined';
    }
  }

  getExportStatusClass(item: any, statusType: string) {
    if (item.indexOf(this.statuses[statusType].success) !== -1) {
      return 'badge badge-pill badge-success';
    } else if (item.indexOf(this.statuses[statusType].started) !== -1) {
      return 'badge badge-pill badge-warning';
    } else {
      return 'badge badge-pill badge-info';
    }
  }

}
