import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Params} from '@angular/router';
import {Title} from '@angular/platform-browser';
import {ApiDataService} from '../api-data.service';

@Component({
  selector: 'app-samples-details',
  templateUrl: './samples-details.component.html',
  styleUrls: ['./samples-details.component.css']
})
export class SamplesDetailsComponent implements OnInit {
  sampleId: string;
  data: any;

  constructor(private route: ActivatedRoute,
              private title: Title,
              private dataService: ApiDataService) { }

  ngOnInit() {
    this.title.setTitle('Sample Logs details');
    this.route.params.subscribe((params: Params) => {
      this.sampleId = params.id;
      this.dataService.getSampleJovian(this.sampleId).subscribe(
      data => {
        this.data = data.results;
      },
      error => {
        console.log(error);
      }
    );
    });
  }

}
