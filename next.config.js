/** @type {import('next').NextConfig} */
const nextConfig = {
    // Other config options...
    typescript: {
      // Dangerously allow production builds to successfully complete even if
      // your project has type errors.
      ignoreBuildErrors: true,
    },
  };
  
  module.exports = nextConfig;
  