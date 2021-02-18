import { environment } from '../../environments/environment';
export const apiUrl = (...paths) => {
    return environment.host + paths.join('/');
};
//# sourceMappingURL=api-url.js.map