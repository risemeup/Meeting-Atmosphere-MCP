#!/usr/bin/env node

const { spawn, execSync } = require('child_process');
const path = require('path');

function checkCommandExists(command) {
  try {
    execSync(`${command} --version`, { stdio: 'ignore' });
    return true;
  } catch {
    return false;
  }
}

async function main() {
  try {
    // Check if uv is installed
    if (!checkCommandExists('uv')) {
      console.error('Error: uv is not installed. Please install uv first: https://docs.astral.sh/uv/');
      process.exit(1);
    }

    // Install dependencies
    console.log('Installing dependencies...');
    const installProcess = spawn('uv', ['sync'], {
      stdio: 'inherit',
      cwd: path.join(__dirname, '..')
    });

    installProcess.on('close', (code) => {
      if (code !== 0) {
        console.error('Failed to install dependencies');
        process.exit(1);
      }

      // Run the MCP server
      console.log('Starting MCP server...');
      const serverProcess = spawn('uv', ['run', 'python', 'server.py'], {
        stdio: 'inherit',
        cwd: path.join(__dirname, '..')
      });

      serverProcess.on('close', (code) => {
        process.exit(code || 0);
      });
    });

  } catch (error) {
    console.error('Failed to start MCP server:', error.message);
    process.exit(1);
  }
}

main();