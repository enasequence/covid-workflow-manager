import { Component, OnInit } from '@angular/core';
import {Title} from '@angular/platform-browser';
import {ApiDataService} from '@services/api-data.service';

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
      success: 'export_finished',
      started: 'export_started'
    }
  };

  summary = {
    ena_import: {
      Success: 0,
      Processing: 0,
      Undefined: 0,
      Failed: 0
    },
    pipeline_analysis: {
      Success: 0,
      Processing: 0,
      Undefined: 0,
      Failed: 0
    },
    ena_export: {
      Success: 0,
      Processing: 0,
      Undefined: 0,
      Failed: 0
    }
  };

  constructor(private title: Title, private dataService: ApiDataService) { }

  ngOnInit() {
    this.title.setTitle('ONT Samples Logs');
    this.dataService.getAllSamplesONT().subscribe(
      data => {
        this.data = data.results;
        if (this.data) {
          this.getSummary(data.results);
        }
      },
      error => {
        console.log(error);
      }
    );
  }

  getSummary(data: any) {
    for (const item of data) {
      const enaImportStatus = this.getExportStatus(item.import_from_ena.status, 'ena_import');
      const pipelineAnalysisStatus = this.getExportStatus(item.pipeline_analysis.status, 'pipeline_analysis');
      const enaExportStatus = this.getExportStatus(item.export_to_ena.status, 'ena_export');
      console.log(enaExportStatus);
      this.summary.ena_import[enaImportStatus] += 1;
      this.summary.pipeline_analysis[pipelineAnalysisStatus] += 1;
      this.summary.ena_export[enaExportStatus] += 1;
    }
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
