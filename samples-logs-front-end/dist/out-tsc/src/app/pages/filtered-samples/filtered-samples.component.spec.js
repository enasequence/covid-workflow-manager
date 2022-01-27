import { async, TestBed } from '@angular/core/testing';
import { FilteredSamplesComponent } from './filtered-samples.component';
describe('FilteredSamplesComponent', () => {
    let component;
    let fixture;
    beforeEach(async(() => {
        TestBed.configureTestingModule({
            declarations: [FilteredSamplesComponent]
        })
            .compileComponents();
    }));
    beforeEach(() => {
        fixture = TestBed.createComponent(FilteredSamplesComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });
    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
//# sourceMappingURL=filtered-samples.component.spec.js.map