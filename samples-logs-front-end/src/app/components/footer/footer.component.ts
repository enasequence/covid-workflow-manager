import { Component, OnInit } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Environment } from 'src/environments/ienvironment';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  public environment: Environment = environment;

  constructor() { }

  ngOnInit() {
  }

}
