<?php

// Create and check connection
$conn = new mysqli('localhost:3306', 'root', '', 'data');
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Choose which method to go with
switch ($_SERVER['REQUEST_METHOD']) {
    case 'GET':
        read_assets();
        break;
    case 'POST':
        create_asset();
        break;
    case 'PUT':
        update_asset();
        break;
    case 'DELETE':
        delete_asset();
        break;
}

// Close connection and exit with 200 OK
$conn->close();
exit(200);

/**
 * Read and return either all assets or one of the assets
 */
function read_assets() {
    // Id is provided, get one
    if (isset($_REQUEST['id'])) {
        $result = $GLOBALS['conn']->query("SELECT * FROM assets WHERE id={$_REQUEST['id']}");
    } else { // Get All
        $result = $GLOBALS['conn']->query("SELECT * FROM assets");
    }
    // Output data
    while($row = $result->fetch_assoc()) {
        echo json_encode($row);
    }
}

/**
 * Create asset if all values are set
 */
function create_asset() {
    $body = $_REQUEST;
    // Check if all params are set
    if (!isset($body['type']) || !isset($body['title']) || !isset($body['label']) || !isset($body['url'])) {
        exit(400); // Bad request
    }

    // Type can only be photo or video
    if (!array_intersect(['photo', 'video'], [$body['type']])) {
        exit(400); // Bad request
    }

    // Insert data, id is set automatically
    if (!$GLOBALS['conn']->query("INSERT INTO assets (type, title, label, url)".
        " VALUES ('{$body['type']}','{$body['title']}','{$body['label']}','{$body['url']}')")) {
        echo "INSERT FAILED";
        exit(400); // Bad request
    }
}

/**
 * Update asset, needs id, updates value provided: title, label and/or url, can't change asset type
 */
function update_asset() {
    // id of updated asset has to be set
    if (!isset($_REQUEST['id'])) {
        exit(400); // Bad request
    }

    $body = json_decode(file_get_contents('php://input'),1);

    // Try to update title, label and url
    foreach (['title', 'label', 'url'] as $col) {
        if (isset($body[$col])) {
            if (!$GLOBALS['conn']->query("UPDATE assets SET $col='{$body[$col]}' WHERE id={$_REQUEST['id']}")) {
                echo "UPDATE FAILED";
                echo(400); // Bad request
            }
        }
    }
}

/**
 * Delete asset, needs id
 */
function delete_asset() {
    // id of deleted asset has to be set
    if (!isset($_REQUEST['id'])) {
        exit(400); # Bad request
    }

    // Delete asset with given id
    if (!$GLOBALS['conn']->query("DELETE FROM assets WHERE id={$_REQUEST['id']}")) {
        echo "DELETE FAILED";
        exit(400); // Bad request
    }
}

