import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Title } from '@angular/platform-browser';
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

  importLogs;
  importErrors;
  pipelineLogs;
  pipelineErrors;
  exportLogs;
  exportErrors;

  constructor(
    private route: ActivatedRoute,
    private title: Title,
    private apiService: ApiService
  ) { }

  ngOnInit() {
    this.title.setTitle('Sample Logs details');
    this.route.params.subscribe((params: Params) => {
      this.pipeline = params.pipeline;
      this.sampleId = params.id;
      this.apiService.getSample(this.pipeline, this.sampleId).subscribe(
      data => {
        console.log(data);
        this.data = data.results;
      },
      error => {
        console.log(error);
      }
    );
    });
  }

}
