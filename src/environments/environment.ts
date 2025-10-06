/* Replace the auth0 values below with your actual Auth0 configuration
 * Get these values from your Auth0 Dashboard:
 * - url: Your Auth0 domain prefix (from Applications > Your SPA > Settings > Domain)
 * - audience: Your API identifier (from Applications > APIs > Your API > Settings > Identifier)
 * - clientId: Your client ID (from Applications > Your SPA > Settings > Client ID)
 */

export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
    url: 'YOUR-TENANT-NAME', // Replace with your Auth0 tenant prefix (e.g., 'dev-abc123')
    audience: 'coffee', // Your API identifier (use 'coffee' as configured)
    clientId: 'YOUR-CLIENT-ID', // Replace with your actual client ID
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application
  }
};
