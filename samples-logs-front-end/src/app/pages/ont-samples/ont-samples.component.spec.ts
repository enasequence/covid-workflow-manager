import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OntSamplesComponent } from './ont-samples.component';

describe('OntSamplesComponent', () => {
  let component: OntSamplesComponent;
  let fixture: ComponentFixture<OntSamplesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OntSamplesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OntSamplesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
