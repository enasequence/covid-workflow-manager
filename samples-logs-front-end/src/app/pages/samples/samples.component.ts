import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { ActivatedRoute } from '@angular/router';
import { map, switchMap } from 'rxjs/operators';

import { TransformService } from '@services/transform.service';
import { SampleLog } from '@models/sample-log';
import { LogSummary } from '@models/log-summary';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-samples',
  templateUrl: './samples.component.html',
  styleUrls: ['./samples.component.css']
})
export class SamplesComponent implements OnInit {
  sampleRuns: Observable<SampleLog[]>;
  pipeline: Observable<string>;
  summary: Observable<LogSummary>;

  constructor(
    private route: ActivatedRoute,
    private title: Title,
    private transformService: TransformService,
  ) { }

  ngOnInit() {

    this.sampleRuns = this.route.paramMap.pipe(
      switchMap(params => {
        this.title.setTitle(`${params.get('pipeline')} Samples`);
        return this.transformService.getSamples(params.get('pipeline'));
      }),
    );
    this.summary = this.sampleRuns.pipe(
      map(this.transformService.summarise),
    );
    this.pipeline = this.route.paramMap.pipe(
      map(x => x.get('pipeline'))
    );

  }

}


