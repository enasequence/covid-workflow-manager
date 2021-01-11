import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { ActivatedRoute } from '@angular/router';
import { map, concatMap, tap } from 'rxjs/operators';

import { ApiService } from '@services/api-mock.service';
import { TransformService } from '@services/transform.service';
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

    this.route.params.pipe(
      map(params => params.pipeline),
      tap(pipeline => {
        this.pipeline = pipeline;
        this.title.setTitle(`${pipeline} Samples`);
      }),
      concatMap(pipeline => this.apiService.get(pipeline)),
      map(response => {
        switch (this.pipeline) {
          case 'jovian':
          case 'jovian_test':
            return this.transformService.extractJovianPipelineStatus(response);
          case 'ont':
            return this.transformService.extractOntPipelineStatus(response);
        }
      }),
    ).subscribe(
      parsedData => {
        this.data = parsedData;
        this.summary = this.transformService.summarise(parsedData);
      },
      console.error
    );

  }

}


