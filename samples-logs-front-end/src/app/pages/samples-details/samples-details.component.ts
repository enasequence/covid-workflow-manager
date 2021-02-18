import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Title } from '@angular/platform-browser';
import { switchMap, map, shareReplay } from 'rxjs/operators';
import { get } from 'lodash/fp';

import { ApiService } from '@services/api-mock.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-samples-details',
  templateUrl: './samples-details.component.html',
  styleUrls: ['./samples-details.component.css']
})
export class SamplesDetailsComponent implements OnInit {
  pipeline: Observable<string>;
  sampleId: Observable<string>;
  sampleRun: Observable<any>;

  constructor(
    private route: ActivatedRoute,
    private title: Title,
    private apiService: ApiService
  ) { }

  ngOnInit() {

    this.sampleRun = this.route.paramMap.pipe(
      switchMap(params => {
        const pipeline = params.get('pipeline');
        const id = params.get('id');

        this.title.setTitle(`${pipeline} details`);
        return this.apiService.getSample(pipeline, id);
      }),
    );

    this.sampleId = this.route.paramMap.pipe(
      map(x => x.get('id'))
    );

    this.pipeline = this.route.paramMap.pipe(
      map(x => x.get('pipeline'))
    );

  }

}
