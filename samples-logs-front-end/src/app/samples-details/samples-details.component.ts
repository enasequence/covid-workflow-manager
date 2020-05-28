import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Params} from "@angular/router";
import {Title} from "@angular/platform-browser";
import {ApiDataService} from "../api-data.service";

@Component({
  selector: 'app-samples-details',
  templateUrl: './samples-details.component.html',
  styleUrls: ['./samples-details.component.css']
})
export class SamplesDetailsComponent implements OnInit {
  sampleId: string;
  sampleData: any;
  data: any;

  constructor(private route: ActivatedRoute,
              private title: Title,
              private dataService: ApiDataService) { }

  ngOnInit() {
    this.title.setTitle('Sample Logs details');
    this.route.params.subscribe((params: Params) => {
      this.sampleId = params.id;
      this.dataService.getAllSamples().subscribe(
      data => {
        this.data = data.results;
        if (this.data) {
          for (const record of this.data) {
        if (record.id === this.sampleId) {
          this.sampleData = record;
        }
        }
        }
      },
      error => {
        console.log(error);
      }
    );
    });
  }

  generateLink() {
    console.log(`http://193.62.54.246/nextflow_reports/${this.sampleId}_output/${this.sampleId}.html`);
    return `http://193.62.54.246/nextflow_reports/${this.sampleId}_output/${this.sampleId}.html`;
  }

}
