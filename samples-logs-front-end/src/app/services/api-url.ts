import { environment } from '../../environments/environment';

export const apiUrl = (...paths: string[]): string => {
  return environment.host + paths.join('/');
};
