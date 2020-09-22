import { Component, OnInit } from '@angular/core';
import {Title} from '@angular/platform-browser';
import {ApiDataService} from '@services/api-data.service';

@Component({
  selector: 'app-samples',
  templateUrl: './samples.component.html',
  styleUrls: ['./samples.component.css']
})
export class SamplesComponent implements OnInit {
  p = 1;
  data: any;
  statuses = {
    ena_import: {
      success: 'download finished',
      failed: 'download failed'
    },
    pipeline_analysis: {
      success: 'pipeline finished',
      failed: 'pipeline finished with errors'
    },
    ena_export: {
      success: 'submission to ENA finished',
      failed: 'submission to ENA failed'
    }
  };

  constructor(private title: Title, private dataService: ApiDataService) { }

  ngOnInit() {
    this.title.setTitle('Samples Logs');
    this.dataService.getMockJovianSamples().subscribe(
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
    } else if (item.indexOf(this.statuses[statusType].failed) !== -1) {
      return 'Failed';
    } else {
      return 'Undefined';
    }
  }

  getExportStatusClass(item: any, statusType: string) {
    if (item.indexOf(this.statuses[statusType].success) !== -1) {
      return 'badge badge-pill badge-success';
    } else if (item.indexOf(this.statuses[statusType].failed) !== -1) {
      return 'badge badge-pill badge-danger';
    } else {
      return 'badge badge-pill badge-info';
    }
  }

}
