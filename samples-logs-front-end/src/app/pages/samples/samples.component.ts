import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { ActivatedRoute } from '@angular/router';
import { map, tap } from 'rxjs/operators';

import { get } from 'lodash/fp';

import { ApiService } from '@services/api-mock.service';
import { TransformService } from '@services/transform.service';
import { ApiResponse } from '@models/api';
import { SampleLog } from '@models/sample-log';
import { LogSummary } from '@models/log-summary';

@Component({
  selector: 'app-samples',
  templateUrl: './samples.component.html',
  styleUrls: ['./samples.component.css']
})
export class SamplesComponent implements OnInit {
  data: SampleLog[];
  pipeline: string;
  filters: {};
  summary: LogSummary = {
    import: {},
    pipeline: {},
    export: {}
  };

  constructor(
    private route: ActivatedRoute,
    private title: Title,
    private apiService: ApiService,
    private transformService: TransformService,
  ) { }

  ngOnInit() {

    this.route.params.subscribe(
      (params) => {
        this.pipeline = params.pipeline;
        this.title.setTitle(`${this.pipeline} Logs`);
        this.getSamples(this.pipeline);
      }
    );

  }

    getSamples(pipeline: string) {

      const extractPipeline = (x: ApiResponse): SampleLog[] => {
        switch (pipeline) {
          case 'jovian':
          case 'jovian_test':
            return this.transformService.extractJovianPipelineStatus(x);
          case 'ont':
            return this.transformService.extractOntPipelineStatus(x);
          default:
            return get('results')(x);
        }
      };

      this.apiService.get(pipeline).pipe(
        tap(console.log),
        map(extractPipeline),
        tap(console.log),
      ).subscribe(
        parsedData => {
          this.data = parsedData;
          this.summary = this.transformService.summarise(parsedData);
        },
        console.error
      );
    }

}
