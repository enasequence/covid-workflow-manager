import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Params} from '@angular/router';
import {Title} from '@angular/platform-browser';
import {ApiService} from '@services/api.service';

@Component({
  selector: 'app-filtered-samples',
  templateUrl: './filtered-samples.component.html',
})
export class FilteredSamplesComponent implements OnInit {
  stage: string;
  status: string;
  data: any;
  p = 1;
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
      success: 'export_finished',
      started: 'export_started'
    }
  };

  constructor(private route: ActivatedRoute,
              private title: Title,
              private dataService: ApiService) { }

  ngOnInit() {
    this.title.setTitle('ONT Samples Logs filtered');
    this.route.params.subscribe((params: Params) => {
      this.stage = params.stage;
      this.status = params.status;
      this.dataService.getFilteredSamplesONT(this.stage, this.status).subscribe(
        data => {
          this.data = data.results;
        },
        error => {
          console.log(error);
        }
      );
    });
  }

  getDate(item: any) {
    return item.split('-')[0];
  }

  getExportStatus(item: any, statusType: string) {
    if (item.indexOf(this.statuses[statusType].success) !== -1) {
      return 'Success';
    } else if (item.indexOf(this.statuses[statusType].started) !== -1) {
      if (this.getAllIndices(item, this.statuses[statusType].started).length >= 6) {
        return 'Failed';
      }
      return 'Processing';
    } else {
      return 'Undefined';
    }
  }

  getAllIndices(arr: any, val: string) {
    const indices = [];
    let i = -1;
    while (arr.indexOf(val, i + 1) !== -1) {
      i = arr.indexOf(val, i + 1);
      indices.push(i);
    }
    return indices;
  }

  getExportStatusClass(item: any, statusType: string) {
    if (item.indexOf(this.statuses[statusType].success) !== -1) {
      return 'badge badge-pill badge-success';
    } else if (item.indexOf(this.statuses[statusType].started) !== -1) {
      if (this.getAllIndices(item, this.statuses[statusType].started).length >= 6) {
        return 'badge badge-pill badge-danger';
      }
      return 'badge badge-pill badge-warning';
    } else {
      return 'badge badge-pill badge-info';
    }
  }


}
