
export const apiUrl = (...paths: string[]): string => {
  const protocol = 'http://';
  const domain = '193.62.54.246';
  return protocol + domain + '/api/' + paths.join('/');
};

