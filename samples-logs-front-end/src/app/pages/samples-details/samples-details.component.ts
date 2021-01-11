import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Title } from '@angular/platform-browser';
import { concatMap, tap } from 'rxjs/operators';

import { ApiService } from '@services/api-mock.service';

@Component({
  selector: 'app-samples-details',
  templateUrl: './samples-details.component.html',
  styleUrls: ['./samples-details.component.css']
})
export class SamplesDetailsComponent implements OnInit {
  pipeline: string;
  sampleId: string;
  data: any;

  constructor(
    private route: ActivatedRoute,
    private title: Title,
    private apiService: ApiService
  ) { }

  ngOnInit() {
    this.route.params.pipe(
      tap(params => {
        this.pipeline = params.pipeline;
        this.sampleId = params.id;
        this.title.setTitle(`${params.id} details`);
      }),
      concatMap(params => this.apiService.getSample(params.pipeline, params.id))
    ).subscribe(
      data => this.data = data.results,
      console.error
    );

  }

}
