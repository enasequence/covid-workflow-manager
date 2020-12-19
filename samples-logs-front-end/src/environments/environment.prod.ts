import { ApiService as ApiMockService } from '@services/api-mock.service';
import { ApiService } from '@services/api.service';

export const environment = {
  production: true,
  name: 'production',
  apiUrl: 'http://193.62.54.246/api/',
  providers: [
    { provide: ApiMockService, useClass: ApiService },
  ],
};
