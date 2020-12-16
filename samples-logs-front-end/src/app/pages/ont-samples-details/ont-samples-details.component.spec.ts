import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OntSamplesDetailsComponent } from './ont-samples-details.component';

describe('OntSamplesDetailsComponent', () => {
  let component: OntSamplesDetailsComponent;
  let fixture: ComponentFixture<OntSamplesDetailsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OntSamplesDetailsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OntSamplesDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
