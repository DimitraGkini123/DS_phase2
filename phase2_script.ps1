$rates = @(50, 70, 90, 110, 130)

$env:NUM_REQUESTS = "500"

New-Item `
    -ItemType Directory `
    -Force `
    -Path ".\logs_phase2" `
    | Out-Null


Write-Host ""
Write-Host "========================================="
Write-Host "Starting Phase 2 experiments"
Write-Host "========================================="
Write-Host ""


# Start Redis and the Phase 2 server
docker compose up -d redis server

Start-Sleep -Seconds 3


foreach ($rate in $rates) {

    Write-Host ""
    Write-Host "-----------------------------------------"
    Write-Host "Phase 2: $rate requests/sec"
    Write-Host "-----------------------------------------"

    $logDir = ".\logs_phase2\$rate"

    New-Item `
        -ItemType Directory `
        -Force `
        -Path $logDir `
        | Out-Null


    # Start every experiment with an empty cache
    docker compose exec -T redis redis-cli FLUSHALL


    # Restart server for a clean run
    docker compose up `
        -d `
        --force-recreate `
        server


    Start-Sleep -Seconds 2


    # Run Phase 2 client
    docker compose run `
        --rm `
        -e SERVER_HOST=server `
        -e REQUEST_RATE=$rate `
        -e NUM_REQUESTS=$env:NUM_REQUESTS `
        client `
        2>&1 |
        Tee-Object `
            -FilePath "$logDir\client.log"


    # Save server logs
    docker compose logs `
        --no-color `
        server `
        > "$logDir\docker.log"


    Start-Sleep -Seconds 2
}


Write-Host ""
Write-Host "========================================="
Write-Host "Phase 2 experiments finished"
Write-Host "========================================="