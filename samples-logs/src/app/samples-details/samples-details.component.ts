import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Params} from "@angular/router";
import {Title} from "@angular/platform-browser";

@Component({
  selector: 'app-samples-details',
  templateUrl: './samples-details.component.html',
  styleUrls: ['./samples-details.component.css']
})
export class SamplesDetailsComponent implements OnInit {
  sampleId: string;

  constructor(private route: ActivatedRoute, private title: Title) { }

  ngOnInit() {
    this.title.setTitle('Sample Logs details');
    this.route.params.subscribe((params: Params) => {
      this.sampleId = params['id'];
    });
  }

}
