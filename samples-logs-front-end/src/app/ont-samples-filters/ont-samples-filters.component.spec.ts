import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OntSamplesFiltersComponent } from './ont-samples-filters.component';

describe('OntSamplesFiltersComponent', () => {
  let component: OntSamplesFiltersComponent;
  let fixture: ComponentFixture<OntSamplesFiltersComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OntSamplesFiltersComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OntSamplesFiltersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
