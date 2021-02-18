import { TestBed } from '@angular/core/testing';
import { ApiDataService } from './api-data.service';
describe('ApiDataService', () => {
    beforeEach(() => TestBed.configureTestingModule({}));
    it('should be created', () => {
        const service = TestBed.get(ApiDataService);
        expect(service).toBeTruthy();
    });
    it('parses test response correctly', () => {
    });
});
//# sourceMappingURL=api-data.service.spec.js.map