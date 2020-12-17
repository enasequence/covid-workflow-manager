import { async, TestBed } from '@angular/core/testing';
import { SamplesDetailsComponent } from './samples-details.component';
describe('SamplesDetailsComponent', () => {
    let component;
    let fixture;
    beforeEach(async(() => {
        TestBed.configureTestingModule({
            declarations: [SamplesDetailsComponent]
        })
            .compileComponents();
    }));
    beforeEach(() => {
        fixture = TestBed.createComponent(SamplesDetailsComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });
    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
//# sourceMappingURL=samples-details.component.spec.js.map