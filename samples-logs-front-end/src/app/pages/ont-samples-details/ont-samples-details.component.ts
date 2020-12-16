import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Params} from '@angular/router';
import {DomSanitizer, Title} from '@angular/platform-browser';
import {ApiDataService} from '@services/api-data.service';

@Component({
  selector: 'app-ont-samples-details',
  templateUrl: './ont-samples-details.component.html',
  styleUrls: ['./ont-samples-details.component.css']
})
export class OntSamplesDetailsComponent implements OnInit {
  sampleId: string;
  data: any;
  reportLink: any;

  constructor(private route: ActivatedRoute,
              private title: Title,
              private dataService: ApiDataService, private sanitizer: DomSanitizer) { }

  ngOnInit() {
    this.title.setTitle('ONT Sample Logs details');
    this.route.params.subscribe((params: Params) => {
      this.sampleId = params.id;
      this.reportLink = `http://193.62.54.246/nextflow_reports/${this.sampleId}_output/${this.sampleId}.html`;
      this.dataService.getSampleONT(this.sampleId).subscribe(
        data => {
          this.data = data.results;
        },
        error => {
          console.log(error);
        }
      );
    });
  }

  generateReport() {
    return this.sanitizer.bypassSecurityTrustResourceUrl(
      `http://193.62.54.246/nextflow_reports/${this.sampleId}_output/${this.sampleId}.html`);
  }

}
