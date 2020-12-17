import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { SampleLog } from '@models/sample-log';
import { LogSummary } from '@models/log-summary';
import { ApiService } from '@services/api.service';
import { MockApiService } from '@services/mock-api.service';
import { map, tap } from 'rxjs/operators';

@Component({
  selector: 'app-ont-samples',
  templateUrl: './ont-samples.component.html',
  styleUrls: ['./ont-samples.component.css']
})
export class OntSamplesComponent implements OnInit {
  p = 1;
  data: SampleLog[];
  summary: LogSummary;

  constructor(
    private title: Title,
    private dataService: ApiService,
    private mock: MockApiService,
  ) { }

  ngOnInit() {
    this.title.setTitle('Nanopore Sample Logs');

    // this.dataService.getAllSamplesONT().subscribe(
    //   data => {
    //     this.data = data.results;
    //     if (this.data) {
    //       this.getSummary(data.results);
    //     }
    //   },
    //   error => {
    //     console.log(error);
    //   }
    // );

    this.mock.getMockOntSamples()
      .pipe(
        map(this.dataService.extractOntPipelineStatus),
      ).subscribe(
      parsedData => {
        this.data = parsedData;
        this.summary = this.dataService.summariseStatuses(parsedData);
      }
    );

  }

}
