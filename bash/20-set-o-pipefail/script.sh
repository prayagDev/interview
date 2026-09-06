#!/bin/bash

set -euo pipefail

DATABASE_URL="some_value"

echo "$DATABASE_URL" | grep "postgres"

echo "Everything worked!"