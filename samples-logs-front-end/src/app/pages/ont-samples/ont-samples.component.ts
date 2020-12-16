import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { ApiDataService } from '@services/api-data.service';
import { MockApiDataService } from '@services/mock-api-data.service';
import { map, tap } from 'rxjs/operators';
import { JobStatus } from '@components/job-status/status';

@Component({
  selector: 'app-ont-samples',
  templateUrl: './ont-samples.component.html',
  styleUrls: ['./ont-samples.component.css']
})
export class OntSamplesComponent implements OnInit {
  p = 1;
  data: any;
  public summary;

  constructor(
    private title: Title,
    private dataService: ApiDataService,
    private mock: MockApiDataService,
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
