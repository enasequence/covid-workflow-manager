import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { ApiService } from '@services/api.service';
import { MockApiService } from '@services/mock-api.service';
import { map, tap } from 'rxjs/operators';

@Component({
  selector: 'app-samples',
  templateUrl: './samples.component.html',
  styleUrls: ['./samples.component.css']
})
export class SamplesComponent implements OnInit {
  p = 1;
  data: any;
  summary;

  constructor(
    private title: Title,
    private dataService: ApiService,
    private mock: MockApiService,
  ) { }

  ngOnInit() {

    this.title.setTitle('Jovian Samples Logs');
    this.dataService.getAllSamplesJovian().pipe(
      map(this.dataService.extractJovianPipelineStatus),
    ).subscribe(
      parsedData => {
        this.data = parsedData;
        this.summary = this.dataService.summariseStatuses(parsedData);
      },
      error => {
        console.log(error);
      }
    );

    // this.mock.getMockJovianSamples()
    //   .pipe(
    //     map(this.dataService.extractJovianPipelineStatus)
    //   ).subscribe(
    //   parsedData => {
    //   sdata = parsedData;
    //     this.summaryi.dataService.summariseStatuses(parsedData);
    //  }

  }

}
