import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Title } from '@angular/platform-browser';
import { map, switchMap } from 'rxjs/operators';

import { TransformService } from '@services/transform.service';
import { Observable } from 'rxjs';
import { SampleLog } from '@models/sample-log';

@Component({
  selector: 'app-filtered-samples',
  templateUrl: './filtered-samples.component.html',
})
export class FilteredSamplesComponent implements OnInit {
  pipeline: Observable<string>;
  stage: Observable<string>;
  status: Observable<string>;
  sampleRuns: Observable<SampleLog[]>;

  constructor(
    private route: ActivatedRoute,
    private title: Title,
    private transformService: TransformService,
  ) { }

  ngOnInit() {

    this.sampleRuns = this.route.paramMap.pipe(
      switchMap(params => {
          this.title.setTitle(`${params.get('pipeline')} filtered samples`);
          return this.transformService.getFilteredSamples(
            params.get('pipeline'),
            params.get('stage'),
            params.get('status')
          );
        })
    );

    this.pipeline = this.route.paramMap.pipe(
      map(params => params.get('pipeline')));

    this.stage = this.route.paramMap.pipe(
      map(params => params.get('stage')));

    this.status = this.route.paramMap.pipe(
      map(params => params.get('status')));

  }

}
