import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Title } from '@angular/platform-browser';
import { concatMap, switchMap, map, tap, shareReplay } from 'rxjs/operators';
import { get } from 'lodash/fp';

import { ApiService } from '@services/api-mock.service';
import { SampleLog } from '@models/sample-log';
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

  getImportLogs(log: SampleLog): string[] {
    return get('import_from_ena.status')(log);
  }

  getImportDates(log: SampleLog): string[] {
    return get('import_from_ena.date')(log);
  }

  ngOnInit() {

    this.sampleRun = this.route.paramMap.pipe(
      switchMap(params => {
        this.title.setTitle(`${params.get('id')} details`);
        return this.apiService.getSample(params.get('pipeline'), params.get('id'));
      }),
      map(get('results')),
      shareReplay(),
    );

    this.sampleId = this.route.paramMap.pipe(
      map(x => x.get('id'))
    );

    this.pipeline = this.route.paramMap.pipe(
      map(x => x.get('pipeline'))
    );

  }

}
