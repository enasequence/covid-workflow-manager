import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { ApiDataService } from '@services/api-data.service';
import { MockApiDataService } from '@services/mock-api-data.service';
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
    private dataService: ApiDataService,
    private mock: MockApiDataService,
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
    //   
 // //
  }

}
