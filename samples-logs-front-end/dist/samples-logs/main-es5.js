function _createForOfIteratorHelper(o) { if (typeof Symbol === "undefined" || o[Symbol.iterator] == null) { if (Array.isArray(o) || (o = _unsupportedIterableToArray(o))) { var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var it, normalCompletion = true, didErr = false, err; return { s: function s() { it = o[Symbol.iterator](); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(n); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["main"], {
  /***/
  "./$$_lazy_route_resource lazy recursive":
  /*!******************************************************!*\
    !*** ./$$_lazy_route_resource lazy namespace object ***!
    \******************************************************/

  /*! no static exports found */

  /***/
  function $$_lazy_route_resourceLazyRecursive(module, exports) {
    function webpackEmptyAsyncContext(req) {
      // Here Promise.resolve().then() is used instead of new Promise() to prevent
      // uncaught exception popping up in devtools
      return Promise.resolve().then(function () {
        var e = new Error("Cannot find module '" + req + "'");
        e.code = 'MODULE_NOT_FOUND';
        throw e;
      });
    }

    webpackEmptyAsyncContext.keys = function () {
      return [];
    };

    webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
    module.exports = webpackEmptyAsyncContext;
    webpackEmptyAsyncContext.id = "./$$_lazy_route_resource lazy recursive";
    /***/
  },

  /***/
  "./node_modules/raw-loader/dist/cjs.js!./src/app/app.component.html":
  /*!**************************************************************************!*\
    !*** ./node_modules/raw-loader/dist/cjs.js!./src/app/app.component.html ***!
    \**************************************************************************/

  /*! exports provided: default */

  /***/
  function node_modulesRawLoaderDistCjsJsSrcAppAppComponentHtml(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = "<router-outlet></router-outlet>\n";
    /***/
  },

  /***/
  "./node_modules/raw-loader/dist/cjs.js!./src/app/header/header.component.html":
  /*!************************************************************************************!*\
    !*** ./node_modules/raw-loader/dist/cjs.js!./src/app/header/header.component.html ***!
    \************************************************************************************/

  /*! exports provided: default */

  /***/
  function node_modulesRawLoaderDistCjsJsSrcAppHeaderHeaderComponentHtml(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = "<nav class=\"navbar navbar-expand-lg navbar-light bg-light\">\n  <a class=\"navbar-brand\" [routerLink]=\"['']\">ENA Workflow Management System</a>\n  <button class=\"navbar-toggler\" type=\"button\" data-toggle=\"collapse\" data-target=\"#navbarNav\" aria-controls=\"navbarNav\" aria-expanded=\"false\" aria-label=\"Toggle navigation\">\n    <span class=\"navbar-toggler-icon\"></span>\n  </button>\n  <div class=\"collapse navbar-collapse\" id=\"navbarNav\">\n    <ul class=\"navbar-nav\">\n      <li class=\"nav-item active\">\n        <a class=\"nav-link\" href=\"#\">Samples logs <span class=\"sr-only\">(current)</span></a>\n      </li>\n      <li class=\"nav-item\">\n        <a class=\"nav-link\"\n           href=\"http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/\" target=\"_blank\">Kubernetes</a>\n      </li>\n    </ul>\n  </div>\n</nav>\n";
    /***/
  },

  /***/
  "./node_modules/raw-loader/dist/cjs.js!./src/app/ont-samples-details/ont-samples-details.component.html":
  /*!**************************************************************************************************************!*\
    !*** ./node_modules/raw-loader/dist/cjs.js!./src/app/ont-samples-details/ont-samples-details.component.html ***!
    \**************************************************************************************************************/

  /*! exports provided: default */

  /***/
  function node_modulesRawLoaderDistCjsJsSrcAppOntSamplesDetailsOntSamplesDetailsComponentHtml(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = "<app-header></app-header>\n<div class=\"container\">\n\n  <div class=\"row\">\n    <div class=\"col-md-12\">\n      <h1 class=\"text-center\">{{sampleId}}</h1>\n    </div>\n  </div>\n\n  <div class=\"row\" *ngIf=\"data\">\n    <div class=\"col-md-12\">\n      <h3>1. ENA import</h3>\n      <h5 *ngIf=\"data['import_from_ena']['status'].length>0\">Logs:</h5>\n      <ul class=\"list-group\">\n        <li\n          class=\"list-group-item list-group-item-success d-flex justify-content-between align-items-center\"\n          *ngFor=\"let date of data['import_from_ena']['date']; let i=index\">\n          {{data['import_from_ena']['status'][i]}}\n          <span class=\"badge badge-primary badge-pill\">{{date}}</span>\n        </li>\n      </ul>\n      <h5 *ngIf=\"data['import_from_ena']['errors'].length>0\">Errors:</h5>\n      <ul class=\"list-group\">\n        <li\n          class=\"list-group-item list-group-item-danger d-flex justify-content-between align-items-center\"\n          *ngFor=\"let error of data['import_from_ena']['errors']\">\n          {{error}}\n        </li>\n      </ul>\n    </div>\n  </div>\n\n  <hr>\n\n  <div class=\"row\" *ngIf=\"data\">\n    <div class=\"col-md-12\">\n      <h3>2. Pipeline run and ENA export reports</h3>\n      <iframe [src]=\"generateReport()\" width=\"100%\" height=980 *ngIf=\"reportLink\">\n      </iframe>\n    </div>\n  </div>\n\n  <hr>\n</div>\n";
    /***/
  },

  /***/
  "./node_modules/raw-loader/dist/cjs.js!./src/app/ont-samples-filters/ont-samples-filters.component.html":
  /*!**************************************************************************************************************!*\
    !*** ./node_modules/raw-loader/dist/cjs.js!./src/app/ont-samples-filters/ont-samples-filters.component.html ***!
    \**************************************************************************************************************/

  /*! exports provided: default */

  /***/
  function node_modulesRawLoaderDistCjsJsSrcAppOntSamplesFiltersOntSamplesFiltersComponentHtml(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = "<app-header></app-header>\n<div class=\"container\">\n\n  <div class=\"row\">\n    <div class=\"col-md-12\">\n      <h3>Runs: </h3>\n    </div>\n  </div>\n\n  <div class=\"row\">\n    <div class=\"col-md-12\">\n      <table class=\"table\">\n        <thead>\n        <tr>\n          <th>Sample ID</th>\n          <th scope=\"col\">Date</th>\n          <th scope=\"col\">Import status</th>\n          <th scope=\"col\">Pipeline status</th>\n          <th>Export status</th>\n        </tr>\n        </thead>\n        <tbody>\n        <tr *ngFor=\"let item of data | paginate: { itemsPerPage: 10, currentPage: p }\">\n          <td><a [routerLink]=\"['/ont', item['id']]\">{{item['id']}}</a></td>\n          <td>{{getDate(item['import_from_ena']['date'][0])}}</td>\n          <td>\n              <span [ngClass]=\"getExportStatusClass(item['import_from_ena']['status'], 'ena_import')\">\n                {{getExportStatus(item['import_from_ena']['status'], 'ena_import')}}\n              </span>\n          </td>\n          <td>\n              <span [ngClass]=\"getExportStatusClass(item['pipeline_analysis']['status'], 'pipeline_analysis')\">\n                {{getExportStatus(item['pipeline_analysis']['status'], 'pipeline_analysis')}}\n              </span>\n          </td>\n          <td>\n              <span [ngClass]=\"getExportStatusClass(item['export_to_ena']['status'], 'ena_export')\">\n                {{getExportStatus(item['export_to_ena']['status'], 'ena_export')}}\n              </span>\n          </td>\n        </tr>\n        </tbody>\n      </table>\n      <pagination-controls (pageChange)=\"p = $event\"></pagination-controls>\n    </div>\n  </div>\n</div>\n";
    /***/
  },

  /***/
  "./node_modules/raw-loader/dist/cjs.js!./src/app/ont-samples/ont-samples.component.html":
  /*!**********************************************************************************************!*\
    !*** ./node_modules/raw-loader/dist/cjs.js!./src/app/ont-samples/ont-samples.component.html ***!
    \**********************************************************************************************/

  /*! exports provided: default */

  /***/
  function node_modulesRawLoaderDistCjsJsSrcAppOntSamplesOntSamplesComponentHtml(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = "<app-header></app-header>\n<div class=\"container\">\n  <div class=\"row\">\n    <div class=\"col-md-12\">\n      <h1>\n        <button type=\"button\" class=\"btn btn-primary\" [routerLink]=\"['/jovian']\">\n          Jovian\n        </button>\n        <button type=\"button\" class=\"btn btn-primary active\" [routerLink]=\"['/ont']\">\n          ONT\n        </button>\n      </h1>\n    </div>\n  </div>\n\n  <hr>\n\n  <div class=\"row\">\n    <div class=\"col-md-12\">\n      <h3>Summary: </h3>\n    </div>\n  </div>\n\n  <div class=\"row\">\n    <div class=\"col-md-4\">\n      <h5>Import status: </h5>\n      <button type=\"button\" class=\"btn btn-success btn-sm\" [routerLink]=\"['import_from_ena', 'Success']\">\n        Success <span class=\"badge badge-light\">{{summary['ena_import']['Success']}}</span>\n      </button>\n      <button type=\"button\" class=\"btn btn-warning btn-sm\" [routerLink]=\"['import_from_ena', 'Processing']\">\n        Processing <span class=\"badge badge-light\">{{summary['ena_import']['Processing']}}</span>\n      </button>\n      <button type=\"button\" class=\"btn btn-primary btn-sm\" [routerLink]=\"['import_from_ena', 'Undefined']\">\n        Undefined <span class=\"badge badge-light\">{{summary['ena_import']['Undefined']}}</span>\n      </button>\n      <button type=\"button\" class=\"btn btn-danger btn-sm\" [routerLink]=\"['import_from_ena', 'Failed']\">\n        Failed <span class=\"badge badge-light\">{{summary['ena_import']['Failed']}}</span>\n      </button>\n    </div>\n    <div class=\"col-md-4\">\n      <h5>Pipeline status: </h5>\n      <button type=\"button\" class=\"btn btn-success btn-sm\" [routerLink]=\"['pipeline_analysis', 'Success']\">\n        Success <span class=\"badge badge-light\">{{summary['pipeline_analysis']['Success']}}</span>\n      </button>\n      <button type=\"button\" class=\"btn btn-warning btn-sm\" [routerLink]=\"['pipeline_analysis', 'Processing']\">\n        Processing <span class=\"badge badge-light\">{{summary['pipeline_analysis']['Processing']}}</span>\n      </button>\n      <button type=\"button\" class=\"btn btn-primary btn-sm\" [routerLink]=\"['pipeline_analysis', 'Undefined']\">\n        Undefined <span class=\"badge badge-light\">{{summary['pipeline_analysis']['Undefined']}}</span>\n      </button>\n      <button type=\"button\" class=\"btn btn-danger btn-sm\" [routerLink]=\"['pipeline_analysis', 'Failed']\">\n        Failed <span class=\"badge badge-light\">{{summary['pipeline_analysis']['Failed']}}</span>\n      </button>\n    </div>\n    <div class=\"col-md-4\">\n      <h5>Export status: </h5>\n      <button type=\"button\" class=\"btn btn-success btn-sm\" [routerLink]=\"['export_to_ena', 'Success']\">\n        Success <span class=\"badge badge-light\">{{summary['ena_export']['Success']}}</span>\n      </button>\n      <button type=\"button\" class=\"btn btn-warning btn-sm\" [routerLink]=\"['export_to_ena', 'Processing']\">\n        Processing <span class=\"badge badge-light\">{{summary['ena_export']['Processing']}}</span>\n      </button>\n      <button type=\"button\" class=\"btn btn-primary btn-sm\" [routerLink]=\"['export_to_ena', 'Undefined']\">\n        Undefined <span class=\"badge badge-light\">{{summary['ena_export']['Undefined']}}</span>\n      </button>\n      <button type=\"button\" class=\"btn btn-danger btn-sm\" [routerLink]=\"['export_to_ena', 'Failed']\">\n        Failed <span class=\"badge badge-light\">{{summary['ena_export']['Failed']}}</span>\n      </button>\n    </div>\n  </div>\n\n  <hr>\n\n  <div class=\"row\">\n    <div class=\"col-md-12\">\n      <h3>Runs: </h3>\n    </div>\n  </div>\n\n  <div class=\"row\">\n    <div class=\"col-md-12\">\n      <table class=\"table\">\n        <thead>\n        <tr>\n          <th>Sample ID</th>\n          <th scope=\"col\">Date</th>\n          <th scope=\"col\">Import status</th>\n          <th scope=\"col\">Pipeline status</th>\n          <th>Export status</th>\n        </tr>\n        </thead>\n        <tbody>\n        <tr *ngFor=\"let item of data | paginate: { itemsPerPage: 10, currentPage: p }\">\n          <td><a [routerLink]=\"item['id']\">{{item['id']}}</a></td>\n          <td>{{getDate(item['import_from_ena']['date'][0])}}</td>\n          <td>\n              <span [ngClass]=\"getExportStatusClass(item['import_from_ena']['status'], 'ena_import')\">\n                {{getExportStatus(item['import_from_ena']['status'], 'ena_import')}}\n              </span>\n          </td>\n          <td>\n              <span [ngClass]=\"getExportStatusClass(item['pipeline_analysis']['status'], 'pipeline_analysis')\">\n                {{getExportStatus(item['pipeline_analysis']['status'], 'pipeline_analysis')}}\n              </span>\n          </td>\n          <td>\n              <span [ngClass]=\"getExportStatusClass(item['export_to_ena']['status'], 'ena_export')\">\n                {{getExportStatus(item['export_to_ena']['status'], 'ena_export')}}\n              </span>\n          </td>\n        </tr>\n        </tbody>\n      </table>\n      <pagination-controls (pageChange)=\"p = $event\"></pagination-controls>\n    </div>\n  </div>\n</div>\n";
    /***/
  },

  /***/
  "./node_modules/raw-loader/dist/cjs.js!./src/app/samples-details/samples-details.component.html":
  /*!******************************************************************************************************!*\
    !*** ./node_modules/raw-loader/dist/cjs.js!./src/app/samples-details/samples-details.component.html ***!
    \******************************************************************************************************/

  /*! exports provided: default */

  /***/
  function node_modulesRawLoaderDistCjsJsSrcAppSamplesDetailsSamplesDetailsComponentHtml(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = "<app-header></app-header>\n<div class=\"container\">\n\n  <div class=\"row\">\n    <div class=\"col-md-12\">\n      <h1 class=\"text-center\">{{sampleId}}</h1>\n    </div>\n  </div>\n\n  <div class=\"row\" *ngIf=\"data\">\n    <div class=\"col-md-12\">\n      <h3>1. ENA import</h3>\n      <h5 *ngIf=\"data['import_from_ena']['status'].length>0\">Logs:</h5>\n      <ul class=\"list-group\">\n        <li\n          class=\"list-group-item list-group-item-success d-flex justify-content-between align-items-center\"\n          *ngFor=\"let date of data['import_from_ena']['date']; let i=index\">\n          {{data['import_from_ena']['status'][i]}}\n          <span class=\"badge badge-primary badge-pill\">{{date}}</span>\n        </li>\n      </ul>\n      <h5 *ngIf=\"data['import_from_ena']['errors'].length>0\">Errors:</h5>\n      <ul class=\"list-group\">\n        <li\n          class=\"list-group-item list-group-item-danger d-flex justify-content-between align-items-center\"\n          *ngFor=\"let error of data['import_from_ena']['errors']\">\n          {{error}}\n        </li>\n      </ul>\n    </div>\n  </div>\n\n  <hr>\n\n  <div class=\"row\" *ngIf=\"data\">\n    <div class=\"col-md-12\">\n      <h3>2. Pipeline run\n      </h3>\n      <h5 *ngIf=\"data['pipeline_analysis']['status'].length>0\">Logs:</h5>\n      <ul class=\"list-group\">\n        <li\n          class=\"list-group-item list-group-item-success d-flex justify-content-between align-items-center\"\n          *ngFor=\"let date of data['pipeline_analysis']['date']; let i=index\">\n          {{data['pipeline_analysis']['status'][i]}}\n          <span class=\"badge badge-primary badge-pill\">{{date}}</span>\n        </li>\n      </ul>\n      <h5 *ngIf=\"data['pipeline_analysis']['errors'].length>0\">Errors:</h5>\n      <ul class=\"list-group\">\n        <li\n          class=\"list-group-item list-group-item-danger d-flex justify-content-between align-items-center\"\n          *ngFor=\"let error of data['pipeline_analysis']['errors']\">\n          {{error}}\n        </li>\n      </ul>\n    </div>\n  </div>\n\n  <hr>\n\n  <div class=\"row\" *ngIf=\"data\">\n    <div class=\"col-md-12\">\n      <h3>3. ENA export</h3>\n      <h5 *ngIf=\"data['export_to_ena']['status'].length>0\">Logs:</h5>\n      <ul class=\"list-group\">\n        <li\n          class=\"list-group-item list-group-item-success d-flex justify-content-between align-items-center\"\n          *ngFor=\"let date of data['export_to_ena']['date']; let i=index\">\n          {{data['export_to_ena']['status'][i]}}\n          <span class=\"badge badge-primary badge-pill\">{{date}}</span>\n        </li>\n      </ul>\n      <h5 *ngIf=\"data['export_to_ena']['errors'].length>0\">Errors:</h5>\n      <ul class=\"list-group\">\n        <li\n          class=\"list-group-item list-group-item-danger d-flex justify-content-between align-items-center\"\n          *ngFor=\"let error of data['export_to_ena']['errors']\">\n          {{error}}\n        </li>\n      </ul>\n    </div>\n  </div>\n</div>\n";
    /***/
  },

  /***/
  "./node_modules/raw-loader/dist/cjs.js!./src/app/samples/samples.component.html":
  /*!**************************************************************************************!*\
    !*** ./node_modules/raw-loader/dist/cjs.js!./src/app/samples/samples.component.html ***!
    \**************************************************************************************/

  /*! exports provided: default */

  /***/
  function node_modulesRawLoaderDistCjsJsSrcAppSamplesSamplesComponentHtml(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = "<app-header></app-header>\n<div class=\"container\">\n  <div class=\"row\">\n    <div class=\"col-md-12\">\n      <h1>\n        <button type=\"button\" class=\"btn btn-primary active\" [routerLink]=\"['/jovian']\">\n          Jovian / Reference\n        </button>\n        <button type=\"button\" class=\"btn btn-primary active\" [routerLink]=\"['/jovian']\">\n          Jovian / Metagenomics\n        </button>\n        <button type=\"button\" class=\"btn btn-primary\" [routerLink]=\"['/ont']\">\n          ONT\n        </button>\n      </h1>\n    </div>\n  </div>\n  <div class=\"row\">\n    <div class=\"col-md-12\">\n      <table class=\"table\">\n        <thead>\n          <tr>\n            <th>Sample ID</th>\n            <th scope=\"col\">Date</th>\n            <th scope=\"col\">Import status</th>\n            <th scope=\"col\">Pipeline status</th>\n            <th>Export status</th>\n          </tr>\n        </thead>\n        <tbody>\n          <tr *ngFor=\"let item of data | paginate: { itemsPerPage: 10, currentPage: p }\">\n            <td><a [routerLink]=\"item['id']\">{{item['id']}}</a></td>\n            <td>{{getDate(item['import_from_ena']['date'][0])}}</td>\n            <td>\n              <span [ngClass]=\"getExportStatusClass(item['import_from_ena']['status'], 'ena_import')\">\n                {{getExportStatus(item['import_from_ena']['status'], 'ena_import')}}\n              </span>\n            </td>\n            <td>\n              <span [ngClass]=\"getExportStatusClass(item['pipeline_analysis']['status'], 'pipeline_analysis')\">\n                {{getExportStatus(item['pipeline_analysis']['status'], 'pipeline_analysis')}}\n              </span>\n            </td>\n            <td>\n              <span [ngClass]=\"getExportStatusClass(item['export_to_ena']['status'], 'ena_export')\">\n                {{getExportStatus(item['export_to_ena']['status'], 'ena_export')}}\n              </span>\n            </td>\n          </tr>\n        </tbody>\n      </table>\n      <pagination-controls (pageChange)=\"p = $event\"></pagination-controls>\n    </div>\n  </div>\n</div>\n";
    /***/
  },

  /***/
  "./node_modules/tslib/tslib.es6.js":
  /*!*****************************************!*\
    !*** ./node_modules/tslib/tslib.es6.js ***!
    \*****************************************/

  /*! exports provided: __extends, __assign, __rest, __decorate, __param, __metadata, __awaiter, __generator, __exportStar, __values, __read, __spread, __spreadArrays, __await, __asyncGenerator, __asyncDelegator, __asyncValues, __makeTemplateObject, __importStar, __importDefault, __classPrivateFieldGet, __classPrivateFieldSet */

  /***/
  function node_modulesTslibTslibEs6Js(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__extends", function () {
      return __extends;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__assign", function () {
      return _assign;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__rest", function () {
      return __rest;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__decorate", function () {
      return __decorate;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__param", function () {
      return __param;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__metadata", function () {
      return __metadata;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__awaiter", function () {
      return __awaiter;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__generator", function () {
      return __generator;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__exportStar", function () {
      return __exportStar;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__values", function () {
      return __values;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__read", function () {
      return __read;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__spread", function () {
      return __spread;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__spreadArrays", function () {
      return __spreadArrays;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__await", function () {
      return __await;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__asyncGenerator", function () {
      return __asyncGenerator;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__asyncDelegator", function () {
      return __asyncDelegator;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__asyncValues", function () {
      return __asyncValues;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__makeTemplateObject", function () {
      return __makeTemplateObject;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__importStar", function () {
      return __importStar;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__importDefault", function () {
      return __importDefault;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__classPrivateFieldGet", function () {
      return __classPrivateFieldGet;
    });
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "__classPrivateFieldSet", function () {
      return __classPrivateFieldSet;
    });
    /*! *****************************************************************************
    Copyright (c) Microsoft Corporation. All rights reserved.
    Licensed under the Apache License, Version 2.0 (the "License"); you may not use
    this file except in compliance with the License. You may obtain a copy of the
    License at http://www.apache.org/licenses/LICENSE-2.0
    
    THIS CODE IS PROVIDED ON AN *AS IS* BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED
    WARRANTIES OR CONDITIONS OF TITLE, FITNESS FOR A PARTICULAR PURPOSE,
    MERCHANTABLITY OR NON-INFRINGEMENT.
    
    See the Apache Version 2.0 License for specific language governing permissions
    and limitations under the License.
    ***************************************************************************** */

    /* global Reflect, Promise */


    var _extendStatics = function extendStatics(d, b) {
      _extendStatics = Object.setPrototypeOf || {
        __proto__: []
      } instanceof Array && function (d, b) {
        d.__proto__ = b;
      } || function (d, b) {
        for (var p in b) {
          if (b.hasOwnProperty(p)) d[p] = b[p];
        }
      };

      return _extendStatics(d, b);
    };

    function __extends(d, b) {
      _extendStatics(d, b);

      function __() {
        this.constructor = d;
      }

      d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    }

    var _assign = function __assign() {
      _assign = Object.assign || function __assign(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
          s = arguments[i];

          for (var p in s) {
            if (Object.prototype.hasOwnProperty.call(s, p)) t[p] = s[p];
          }
        }

        return t;
      };

      return _assign.apply(this, arguments);
    };

    function __rest(s, e) {
      var t = {};

      for (var p in s) {
        if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0) t[p] = s[p];
      }

      if (s != null && typeof Object.getOwnPropertySymbols === "function") for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
        if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i])) t[p[i]] = s[p[i]];
      }
      return t;
    }

    function __decorate(decorators, target, key, desc) {
      var c = arguments.length,
          r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc,
          d;
      if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);else for (var i = decorators.length - 1; i >= 0; i--) {
        if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
      }
      return c > 3 && r && Object.defineProperty(target, key, r), r;
    }

    function __param(paramIndex, decorator) {
      return function (target, key) {
        decorator(target, key, paramIndex);
      };
    }

    function __metadata(metadataKey, metadataValue) {
      if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(metadataKey, metadataValue);
    }

    function __awaiter(thisArg, _arguments, P, generator) {
      function adopt(value) {
        return value instanceof P ? value : new P(function (resolve) {
          resolve(value);
        });
      }

      return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) {
          try {
            step(generator.next(value));
          } catch (e) {
            reject(e);
          }
        }

        function rejected(value) {
          try {
            step(generator["throw"](value));
          } catch (e) {
            reject(e);
          }
        }

        function step(result) {
          result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected);
        }

        step((generator = generator.apply(thisArg, _arguments || [])).next());
      });
    }

    function __generator(thisArg, body) {
      var _ = {
        label: 0,
        sent: function sent() {
          if (t[0] & 1) throw t[1];
          return t[1];
        },
        trys: [],
        ops: []
      },
          f,
          y,
          t,
          g;
      return g = {
        next: verb(0),
        "throw": verb(1),
        "return": verb(2)
      }, typeof Symbol === "function" && (g[Symbol.iterator] = function () {
        return this;
      }), g;

      function verb(n) {
        return function (v) {
          return step([n, v]);
        };
      }

      function step(op) {
        if (f) throw new TypeError("Generator is already executing.");

        while (_) {
          try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];

            switch (op[0]) {
              case 0:
              case 1:
                t = op;
                break;

              case 4:
                _.label++;
                return {
                  value: op[1],
                  done: false
                };

              case 5:
                _.label++;
                y = op[1];
                op = [0];
                continue;

              case 7:
                op = _.ops.pop();

                _.trys.pop();

                continue;

              default:
                if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) {
                  _ = 0;
                  continue;
                }

                if (op[0] === 3 && (!t || op[1] > t[0] && op[1] < t[3])) {
                  _.label = op[1];
                  break;
                }

                if (op[0] === 6 && _.label < t[1]) {
                  _.label = t[1];
                  t = op;
                  break;
                }

                if (t && _.label < t[2]) {
                  _.label = t[2];

                  _.ops.push(op);

                  break;
                }

                if (t[2]) _.ops.pop();

                _.trys.pop();

                continue;
            }

            op = body.call(thisArg, _);
          } catch (e) {
            op = [6, e];
            y = 0;
          } finally {
            f = t = 0;
          }
        }

        if (op[0] & 5) throw op[1];
        return {
          value: op[0] ? op[1] : void 0,
          done: true
        };
      }
    }

    function __exportStar(m, exports) {
      for (var p in m) {
        if (!exports.hasOwnProperty(p)) exports[p] = m[p];
      }
    }

    function __values(o) {
      var s = typeof Symbol === "function" && Symbol.iterator,
          m = s && o[s],
          i = 0;
      if (m) return m.call(o);
      if (o && typeof o.length === "number") return {
        next: function next() {
          if (o && i >= o.length) o = void 0;
          return {
            value: o && o[i++],
            done: !o
          };
        }
      };
      throw new TypeError(s ? "Object is not iterable." : "Symbol.iterator is not defined.");
    }

    function __read(o, n) {
      var m = typeof Symbol === "function" && o[Symbol.iterator];
      if (!m) return o;
      var i = m.call(o),
          r,
          ar = [],
          e;

      try {
        while ((n === void 0 || n-- > 0) && !(r = i.next()).done) {
          ar.push(r.value);
        }
      } catch (error) {
        e = {
          error: error
        };
      } finally {
        try {
          if (r && !r.done && (m = i["return"])) m.call(i);
        } finally {
          if (e) throw e.error;
        }
      }

      return ar;
    }

    function __spread() {
      for (var ar = [], i = 0; i < arguments.length; i++) {
        ar = ar.concat(__read(arguments[i]));
      }

      return ar;
    }

    function __spreadArrays() {
      for (var s = 0, i = 0, il = arguments.length; i < il; i++) {
        s += arguments[i].length;
      }

      for (var r = Array(s), k = 0, i = 0; i < il; i++) {
        for (var a = arguments[i], j = 0, jl = a.length; j < jl; j++, k++) {
          r[k] = a[j];
        }
      }

      return r;
    }

    ;

    function __await(v) {
      return this instanceof __await ? (this.v = v, this) : new __await(v);
    }

    function __asyncGenerator(thisArg, _arguments, generator) {
      if (!Symbol.asyncIterator) throw new TypeError("Symbol.asyncIterator is not defined.");
      var g = generator.apply(thisArg, _arguments || []),
          i,
          q = [];
      return i = {}, verb("next"), verb("throw"), verb("return"), i[Symbol.asyncIterator] = function () {
        return this;
      }, i;

      function verb(n) {
        if (g[n]) i[n] = function (v) {
          return new Promise(function (a, b) {
            q.push([n, v, a, b]) > 1 || resume(n, v);
          });
        };
      }

      function resume(n, v) {
        try {
          step(g[n](v));
        } catch (e) {
          settle(q[0][3], e);
        }
      }

      function step(r) {
        r.value instanceof __await ? Promise.resolve(r.value.v).then(fulfill, reject) : settle(q[0][2], r);
      }

      function fulfill(value) {
        resume("next", value);
      }

      function reject(value) {
        resume("throw", value);
      }

      function settle(f, v) {
        if (f(v), q.shift(), q.length) resume(q[0][0], q[0][1]);
      }
    }

    function __asyncDelegator(o) {
      var i, p;
      return i = {}, verb("next"), verb("throw", function (e) {
        throw e;
      }), verb("return"), i[Symbol.iterator] = function () {
        return this;
      }, i;

      function verb(n, f) {
        i[n] = o[n] ? function (v) {
          return (p = !p) ? {
            value: __await(o[n](v)),
            done: n === "return"
          } : f ? f(v) : v;
        } : f;
      }
    }

    function __asyncValues(o) {
      if (!Symbol.asyncIterator) throw new TypeError("Symbol.asyncIterator is not defined.");
      var m = o[Symbol.asyncIterator],
          i;
      return m ? m.call(o) : (o = typeof __values === "function" ? __values(o) : o[Symbol.iterator](), i = {}, verb("next"), verb("throw"), verb("return"), i[Symbol.asyncIterator] = function () {
        return this;
      }, i);

      function verb(n) {
        i[n] = o[n] && function (v) {
          return new Promise(function (resolve, reject) {
            v = o[n](v), settle(resolve, reject, v.done, v.value);
          });
        };
      }

      function settle(resolve, reject, d, v) {
        Promise.resolve(v).then(function (v) {
          resolve({
            value: v,
            done: d
          });
        }, reject);
      }
    }

    function __makeTemplateObject(cooked, raw) {
      if (Object.defineProperty) {
        Object.defineProperty(cooked, "raw", {
          value: raw
        });
      } else {
        cooked.raw = raw;
      }

      return cooked;
    }

    ;

    function __importStar(mod) {
      if (mod && mod.__esModule) return mod;
      var result = {};
      if (mod != null) for (var k in mod) {
        if (Object.hasOwnProperty.call(mod, k)) result[k] = mod[k];
      }
      result["default"] = mod;
      return result;
    }

    function __importDefault(mod) {
      return mod && mod.__esModule ? mod : {
        "default": mod
      };
    }

    function __classPrivateFieldGet(receiver, privateMap) {
      if (!privateMap.has(receiver)) {
        throw new TypeError("attempted to get private field on non-instance");
      }

      return privateMap.get(receiver);
    }

    function __classPrivateFieldSet(receiver, privateMap, value) {
      if (!privateMap.has(receiver)) {
        throw new TypeError("attempted to set private field on non-instance");
      }

      privateMap.set(receiver, value);
      return value;
    }
    /***/

  },

  /***/
  "./src/app/app-routing.module.ts":
  /*!***************************************!*\
    !*** ./src/app/app-routing.module.ts ***!
    \***************************************/

  /*! exports provided: AppRoutingModule */

  /***/
  function srcAppAppRoutingModuleTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "AppRoutingModule", function () {
      return AppRoutingModule;
    });
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js");
    /* harmony import */


    var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
    /*! @angular/core */
    "./node_modules/@angular/core/fesm2015/core.js");
    /* harmony import */


    var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(
    /*! @angular/router */
    "./node_modules/@angular/router/fesm2015/router.js");
    /* harmony import */


    var _samples_details_samples_details_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(
    /*! ./samples-details/samples-details.component */
    "./src/app/samples-details/samples-details.component.ts");
    /* harmony import */


    var _samples_samples_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(
    /*! ./samples/samples.component */
    "./src/app/samples/samples.component.ts");
    /* harmony import */


    var _ont_samples_ont_samples_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(
    /*! ./ont-samples/ont-samples.component */
    "./src/app/ont-samples/ont-samples.component.ts");
    /* harmony import */


    var _ont_samples_details_ont_samples_details_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(
    /*! ./ont-samples-details/ont-samples-details.component */
    "./src/app/ont-samples-details/ont-samples-details.component.ts");
    /* harmony import */


    var _ont_samples_filters_ont_samples_filters_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(
    /*! ./ont-samples-filters/ont-samples-filters.component */
    "./src/app/ont-samples-filters/ont-samples-filters.component.ts");

    var routes = [{
      path: '',
      redirectTo: 'jovian',
      pathMatch: 'full'
    }, {
      path: 'jovian',
      component: _samples_samples_component__WEBPACK_IMPORTED_MODULE_4__["SamplesComponent"]
    }, {
      path: 'jovian/:id',
      component: _samples_details_samples_details_component__WEBPACK_IMPORTED_MODULE_3__["SamplesDetailsComponent"]
    }, {
      path: 'ont',
      component: _ont_samples_ont_samples_component__WEBPACK_IMPORTED_MODULE_5__["OntSamplesComponent"]
    }, {
      path: 'ont/:id',
      component: _ont_samples_details_ont_samples_details_component__WEBPACK_IMPORTED_MODULE_6__["OntSamplesDetailsComponent"]
    }, {
      path: 'ont/:stage/:status',
      component: _ont_samples_filters_ont_samples_filters_component__WEBPACK_IMPORTED_MODULE_7__["OntSamplesFiltersComponent"]
    }];

    var AppRoutingModule = function AppRoutingModule() {
      _classCallCheck(this, AppRoutingModule);
    };

    AppRoutingModule = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"])({
      imports: [_angular_router__WEBPACK_IMPORTED_MODULE_2__["RouterModule"].forRoot(routes)],
      exports: [_angular_router__WEBPACK_IMPORTED_MODULE_2__["RouterModule"]]
    })], AppRoutingModule);
    /***/
  },

  /***/
  "./src/app/app.component.css":
  /*!***********************************!*\
    !*** ./src/app/app.component.css ***!
    \***********************************/

  /*! exports provided: default */

  /***/
  function srcAppAppComponentCss(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = "\n\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2FwcC5jb21wb25lbnQuY3NzIn0= */";
    /***/
  },

  /***/
  "./src/app/app.component.ts":
  /*!**********************************!*\
    !*** ./src/app/app.component.ts ***!
    \**********************************/

  /*! exports provided: AppComponent */

  /***/
  function srcAppAppComponentTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "AppComponent", function () {
      return AppComponent;
    });
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js");
    /* harmony import */


    var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
    /*! @angular/core */
    "./node_modules/@angular/core/fesm2015/core.js");

    var AppComponent = function AppComponent() {
      _classCallCheck(this, AppComponent);

      this.title = 'samples-logs';
    };

    AppComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
      selector: 'app-root',
      template: tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! raw-loader!./app.component.html */
      "./node_modules/raw-loader/dist/cjs.js!./src/app/app.component.html"))["default"],
      styles: [tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! ./app.component.css */
      "./src/app/app.component.css"))["default"]]
    })], AppComponent);
    /***/
  },

  /***/
  "./src/app/app.module.ts":
  /*!*******************************!*\
    !*** ./src/app/app.module.ts ***!
    \*******************************/

  /*! exports provided: AppModule */

  /***/
  function srcAppAppModuleTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "AppModule", function () {
      return AppModule;
    });
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js");
    /* harmony import */


    var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
    /*! @angular/platform-browser */
    "./node_modules/@angular/platform-browser/fesm2015/platform-browser.js");
    /* harmony import */


    var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(
    /*! @angular/core */
    "./node_modules/@angular/core/fesm2015/core.js");
    /* harmony import */


    var _app_routing_module__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(
    /*! ./app-routing.module */
    "./src/app/app-routing.module.ts");
    /* harmony import */


    var _app_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(
    /*! ./app.component */
    "./src/app/app.component.ts");
    /* harmony import */


    var _samples_details_samples_details_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(
    /*! ./samples-details/samples-details.component */
    "./src/app/samples-details/samples-details.component.ts");
    /* harmony import */


    var _header_header_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(
    /*! ./header/header.component */
    "./src/app/header/header.component.ts");
    /* harmony import */


    var _samples_samples_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(
    /*! ./samples/samples.component */
    "./src/app/samples/samples.component.ts");
    /* harmony import */


    var ngx_pagination__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(
    /*! ngx-pagination */
    "./node_modules/ngx-pagination/dist/ngx-pagination.js");
    /* harmony import */


    var _services_api_data_service__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(
    /*! ./services/api-data.service */
    "./src/app/services/api-data.service.ts");
    /* harmony import */


    var _angular_common_http__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(
    /*! @angular/common/http */
    "./node_modules/@angular/common/fesm2015/http.js");
    /* harmony import */


    var _ont_samples_ont_samples_component__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(
    /*! ./ont-samples/ont-samples.component */
    "./src/app/ont-samples/ont-samples.component.ts");
    /* harmony import */


    var _ont_samples_details_ont_samples_details_component__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(
    /*! ./ont-samples-details/ont-samples-details.component */
    "./src/app/ont-samples-details/ont-samples-details.component.ts");
    /* harmony import */


    var _ont_samples_filters_ont_samples_filters_component__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(
    /*! ./ont-samples-filters/ont-samples-filters.component */
    "./src/app/ont-samples-filters/ont-samples-filters.component.ts");

    var AppModule = function AppModule() {
      _classCallCheck(this, AppModule);
    };

    AppModule = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([Object(_angular_core__WEBPACK_IMPORTED_MODULE_2__["NgModule"])({
      declarations: [_app_component__WEBPACK_IMPORTED_MODULE_4__["AppComponent"], _samples_details_samples_details_component__WEBPACK_IMPORTED_MODULE_5__["SamplesDetailsComponent"], _header_header_component__WEBPACK_IMPORTED_MODULE_6__["HeaderComponent"], _samples_samples_component__WEBPACK_IMPORTED_MODULE_7__["SamplesComponent"], _ont_samples_ont_samples_component__WEBPACK_IMPORTED_MODULE_11__["OntSamplesComponent"], _ont_samples_details_ont_samples_details_component__WEBPACK_IMPORTED_MODULE_12__["OntSamplesDetailsComponent"], _ont_samples_filters_ont_samples_filters_component__WEBPACK_IMPORTED_MODULE_13__["OntSamplesFiltersComponent"]],
      imports: [_angular_platform_browser__WEBPACK_IMPORTED_MODULE_1__["BrowserModule"], _app_routing_module__WEBPACK_IMPORTED_MODULE_3__["AppRoutingModule"], ngx_pagination__WEBPACK_IMPORTED_MODULE_8__["NgxPaginationModule"], _angular_common_http__WEBPACK_IMPORTED_MODULE_10__["HttpClientModule"]],
      providers: [_services_api_data_service__WEBPACK_IMPORTED_MODULE_9__["ApiDataService"]],
      bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_4__["AppComponent"]]
    })], AppModule);
    /***/
  },

  /***/
  "./src/app/header/header.component.css":
  /*!*********************************************!*\
    !*** ./src/app/header/header.component.css ***!
    \*********************************************/

  /*! exports provided: default */

  /***/
  function srcAppHeaderHeaderComponentCss(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = ".navbar-brand {\n  color: green;\n}\n\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvaGVhZGVyL2hlYWRlci5jb21wb25lbnQuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBO0VBQ0UsWUFBWTtBQUNkIiwiZmlsZSI6InNyYy9hcHAvaGVhZGVyL2hlYWRlci5jb21wb25lbnQuY3NzIiwic291cmNlc0NvbnRlbnQiOlsiLm5hdmJhci1icmFuZCB7XG4gIGNvbG9yOiBncmVlbjtcbn1cbiJdfQ== */";
    /***/
  },

  /***/
  "./src/app/header/header.component.ts":
  /*!********************************************!*\
    !*** ./src/app/header/header.component.ts ***!
    \********************************************/

  /*! exports provided: HeaderComponent */

  /***/
  function srcAppHeaderHeaderComponentTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "HeaderComponent", function () {
      return HeaderComponent;
    });
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js");
    /* harmony import */


    var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
    /*! @angular/core */
    "./node_modules/@angular/core/fesm2015/core.js");

    var HeaderComponent = /*#__PURE__*/function () {
      function HeaderComponent() {
        _classCallCheck(this, HeaderComponent);
      }

      _createClass(HeaderComponent, [{
        key: "ngOnInit",
        value: function ngOnInit() {}
      }]);

      return HeaderComponent;
    }();

    HeaderComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
      selector: 'app-header',
      template: tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! raw-loader!./header.component.html */
      "./node_modules/raw-loader/dist/cjs.js!./src/app/header/header.component.html"))["default"],
      styles: [tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! ./header.component.css */
      "./src/app/header/header.component.css"))["default"]]
    })], HeaderComponent);
    /***/
  },

  /***/
  "./src/app/ont-samples-details/ont-samples-details.component.css":
  /*!***********************************************************************!*\
    !*** ./src/app/ont-samples-details/ont-samples-details.component.css ***!
    \***********************************************************************/

  /*! exports provided: default */

  /***/
  function srcAppOntSamplesDetailsOntSamplesDetailsComponentCss(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL29udC1zYW1wbGVzLWRldGFpbHMvb250LXNhbXBsZXMtZGV0YWlscy5jb21wb25lbnQuY3NzIn0= */";
    /***/
  },

  /***/
  "./src/app/ont-samples-details/ont-samples-details.component.ts":
  /*!**********************************************************************!*\
    !*** ./src/app/ont-samples-details/ont-samples-details.component.ts ***!
    \**********************************************************************/

  /*! exports provided: OntSamplesDetailsComponent */

  /***/
  function srcAppOntSamplesDetailsOntSamplesDetailsComponentTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "OntSamplesDetailsComponent", function () {
      return OntSamplesDetailsComponent;
    });
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js");
    /* harmony import */


    var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
    /*! @angular/core */
    "./node_modules/@angular/core/fesm2015/core.js");
    /* harmony import */


    var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(
    /*! @angular/router */
    "./node_modules/@angular/router/fesm2015/router.js");
    /* harmony import */


    var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(
    /*! @angular/platform-browser */
    "./node_modules/@angular/platform-browser/fesm2015/platform-browser.js");
    /* harmony import */


    var _services_api_data_service__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(
    /*! @services/api-data.service */
    "./src/app/services/api-data.service.ts");

    var OntSamplesDetailsComponent = /*#__PURE__*/function () {
      function OntSamplesDetailsComponent(route, title, dataService, sanitizer) {
        _classCallCheck(this, OntSamplesDetailsComponent);

        this.route = route;
        this.title = title;
        this.dataService = dataService;
        this.sanitizer = sanitizer;
      }

      _createClass(OntSamplesDetailsComponent, [{
        key: "ngOnInit",
        value: function ngOnInit() {
          var _this = this;

          this.title.setTitle('ONT Sample Logs details');
          this.route.params.subscribe(function (params) {
            _this.sampleId = params.id;
            _this.reportLink = "http://193.62.54.246/nextflow_reports/".concat(_this.sampleId, "_output/").concat(_this.sampleId, ".html");

            _this.dataService.getSampleONT(_this.sampleId).subscribe(function (data) {
              _this.data = data.results;
            }, function (error) {
              console.log(error);
            });
          });
        }
      }, {
        key: "generateReport",
        value: function generateReport() {
          return this.sanitizer.bypassSecurityTrustResourceUrl("http://193.62.54.246/nextflow_reports/".concat(this.sampleId, "_output/").concat(this.sampleId, ".html"));
        }
      }]);

      return OntSamplesDetailsComponent;
    }();

    OntSamplesDetailsComponent.ctorParameters = function () {
      return [{
        type: _angular_router__WEBPACK_IMPORTED_MODULE_2__["ActivatedRoute"]
      }, {
        type: _angular_platform_browser__WEBPACK_IMPORTED_MODULE_3__["Title"]
      }, {
        type: _services_api_data_service__WEBPACK_IMPORTED_MODULE_4__["ApiDataService"]
      }, {
        type: _angular_platform_browser__WEBPACK_IMPORTED_MODULE_3__["DomSanitizer"]
      }];
    };

    OntSamplesDetailsComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
      selector: 'app-ont-samples-details',
      template: tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! raw-loader!./ont-samples-details.component.html */
      "./node_modules/raw-loader/dist/cjs.js!./src/app/ont-samples-details/ont-samples-details.component.html"))["default"],
      styles: [tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! ./ont-samples-details.component.css */
      "./src/app/ont-samples-details/ont-samples-details.component.css"))["default"]]
    })], OntSamplesDetailsComponent);
    /***/
  },

  /***/
  "./src/app/ont-samples-filters/ont-samples-filters.component.css":
  /*!***********************************************************************!*\
    !*** ./src/app/ont-samples-filters/ont-samples-filters.component.css ***!
    \***********************************************************************/

  /*! exports provided: default */

  /***/
  function srcAppOntSamplesFiltersOntSamplesFiltersComponentCss(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL29udC1zYW1wbGVzLWZpbHRlcnMvb250LXNhbXBsZXMtZmlsdGVycy5jb21wb25lbnQuY3NzIn0= */";
    /***/
  },

  /***/
  "./src/app/ont-samples-filters/ont-samples-filters.component.ts":
  /*!**********************************************************************!*\
    !*** ./src/app/ont-samples-filters/ont-samples-filters.component.ts ***!
    \**********************************************************************/

  /*! exports provided: OntSamplesFiltersComponent */

  /***/
  function srcAppOntSamplesFiltersOntSamplesFiltersComponentTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "OntSamplesFiltersComponent", function () {
      return OntSamplesFiltersComponent;
    });
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js");
    /* harmony import */


    var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
    /*! @angular/core */
    "./node_modules/@angular/core/fesm2015/core.js");
    /* harmony import */


    var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(
    /*! @angular/router */
    "./node_modules/@angular/router/fesm2015/router.js");
    /* harmony import */


    var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(
    /*! @angular/platform-browser */
    "./node_modules/@angular/platform-browser/fesm2015/platform-browser.js");
    /* harmony import */


    var _services_api_data_service__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(
    /*! @services/api-data.service */
    "./src/app/services/api-data.service.ts");

    var OntSamplesFiltersComponent = /*#__PURE__*/function () {
      function OntSamplesFiltersComponent(route, title, dataService) {
        _classCallCheck(this, OntSamplesFiltersComponent);

        this.route = route;
        this.title = title;
        this.dataService = dataService;
        this.p = 1;
        this.statuses = {
          ena_import: {
            success: 'download finished',
            failed: 'download failed'
          },
          pipeline_analysis: {
            success: 'pipeline_finished',
            started: 'pipeline_started'
          },
          ena_export: {
            success: 'export_finished',
            started: 'export_started'
          }
        };
      }

      _createClass(OntSamplesFiltersComponent, [{
        key: "ngOnInit",
        value: function ngOnInit() {
          var _this2 = this;

          this.title.setTitle('ONT Samples Logs filtered');
          this.route.params.subscribe(function (params) {
            _this2.stage = params.stage;
            _this2.status = params.status;

            _this2.dataService.getFilteredSamplesONT(_this2.stage, _this2.status).subscribe(function (data) {
              _this2.data = data.results;
              console.log(data);
            }, function (error) {
              console.log(error);
            });
          });
        }
      }, {
        key: "getDate",
        value: function getDate(item) {
          return item.split('-')[0];
        }
      }, {
        key: "getExportStatus",
        value: function getExportStatus(item, statusType) {
          if (item.indexOf(this.statuses[statusType].success) !== -1) {
            return 'Success';
          } else if (item.indexOf(this.statuses[statusType].started) !== -1) {
            if (this.getAllIndices(item, this.statuses[statusType].started).length >= 6) {
              return 'Failed';
            }

            return 'Processing';
          } else {
            return 'Undefined';
          }
        }
      }, {
        key: "getAllIndices",
        value: function getAllIndices(arr, val) {
          var indices = [];
          var i = -1;

          while (arr.indexOf(val, i + 1) !== -1) {
            i = arr.indexOf(val, i + 1);
            indices.push(i);
          }

          return indices;
        }
      }, {
        key: "getExportStatusClass",
        value: function getExportStatusClass(item, statusType) {
          if (item.indexOf(this.statuses[statusType].success) !== -1) {
            return 'badge badge-pill badge-success';
          } else if (item.indexOf(this.statuses[statusType].started) !== -1) {
            if (this.getAllIndices(item, this.statuses[statusType].started).length >= 6) {
              return 'badge badge-pill badge-danger';
            }

            return 'badge badge-pill badge-warning';
          } else {
            return 'badge badge-pill badge-info';
          }
        }
      }]);

      return OntSamplesFiltersComponent;
    }();

    OntSamplesFiltersComponent.ctorParameters = function () {
      return [{
        type: _angular_router__WEBPACK_IMPORTED_MODULE_2__["ActivatedRoute"]
      }, {
        type: _angular_platform_browser__WEBPACK_IMPORTED_MODULE_3__["Title"]
      }, {
        type: _services_api_data_service__WEBPACK_IMPORTED_MODULE_4__["ApiDataService"]
      }];
    };

    OntSamplesFiltersComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
      selector: 'app-ont-samples-filters',
      template: tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! raw-loader!./ont-samples-filters.component.html */
      "./node_modules/raw-loader/dist/cjs.js!./src/app/ont-samples-filters/ont-samples-filters.component.html"))["default"],
      styles: [tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! ./ont-samples-filters.component.css */
      "./src/app/ont-samples-filters/ont-samples-filters.component.css"))["default"]]
    })], OntSamplesFiltersComponent);
    /***/
  },

  /***/
  "./src/app/ont-samples/ont-samples.component.css":
  /*!*******************************************************!*\
    !*** ./src/app/ont-samples/ont-samples.component.css ***!
    \*******************************************************/

  /*! exports provided: default */

  /***/
  function srcAppOntSamplesOntSamplesComponentCss(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = "button {\n  margin-left: 5px;\n  margin-bottom: 5px;\n}\n\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvb250LXNhbXBsZXMvb250LXNhbXBsZXMuY29tcG9uZW50LmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtFQUNFLGdCQUFnQjtFQUNoQixrQkFBa0I7QUFDcEIiLCJmaWxlIjoic3JjL2FwcC9vbnQtc2FtcGxlcy9vbnQtc2FtcGxlcy5jb21wb25lbnQuY3NzIiwic291cmNlc0NvbnRlbnQiOlsiYnV0dG9uIHtcbiAgbWFyZ2luLWxlZnQ6IDVweDtcbiAgbWFyZ2luLWJvdHRvbTogNXB4O1xufVxuIl19 */";
    /***/
  },

  /***/
  "./src/app/ont-samples/ont-samples.component.ts":
  /*!******************************************************!*\
    !*** ./src/app/ont-samples/ont-samples.component.ts ***!
    \******************************************************/

  /*! exports provided: OntSamplesComponent */

  /***/
  function srcAppOntSamplesOntSamplesComponentTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "OntSamplesComponent", function () {
      return OntSamplesComponent;
    });
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js");
    /* harmony import */


    var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
    /*! @angular/core */
    "./node_modules/@angular/core/fesm2015/core.js");
    /* harmony import */


    var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(
    /*! @angular/platform-browser */
    "./node_modules/@angular/platform-browser/fesm2015/platform-browser.js");
    /* harmony import */


    var _services_api_data_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(
    /*! @services/api-data.service */
    "./src/app/services/api-data.service.ts");

    var OntSamplesComponent = /*#__PURE__*/function () {
      function OntSamplesComponent(title, dataService) {
        _classCallCheck(this, OntSamplesComponent);

        this.title = title;
        this.dataService = dataService;
        this.p = 1;
        this.statuses = {
          ena_import: {
            success: 'download finished',
            failed: 'download failed'
          },
          pipeline_analysis: {
            success: 'pipeline_finished',
            started: 'pipeline_started'
          },
          ena_export: {
            success: 'export_finished',
            started: 'export_started'
          }
        };
        this.summary = {
          ena_import: {
            Success: 0,
            Processing: 0,
            Undefined: 0,
            Failed: 0
          },
          pipeline_analysis: {
            Success: 0,
            Processing: 0,
            Undefined: 0,
            Failed: 0
          },
          ena_export: {
            Success: 0,
            Processing: 0,
            Undefined: 0,
            Failed: 0
          }
        };
      }

      _createClass(OntSamplesComponent, [{
        key: "ngOnInit",
        value: function ngOnInit() {
          var _this3 = this;

          this.title.setTitle('ONT Samples Logs');
          this.dataService.getAllSamplesONT().subscribe(function (data) {
            _this3.data = data.results;

            if (_this3.data) {
              _this3.getSummary(data.results);
            }
          }, function (error) {
            console.log(error);
          });
        }
      }, {
        key: "getSummary",
        value: function getSummary(data) {
          var _iterator = _createForOfIteratorHelper(data),
              _step;

          try {
            for (_iterator.s(); !(_step = _iterator.n()).done;) {
              var item = _step.value;
              var enaImportStatus = this.getExportStatus(item.import_from_ena.status, 'ena_import');
              var pipelineAnalysisStatus = this.getExportStatus(item.pipeline_analysis.status, 'pipeline_analysis');
              var enaExportStatus = this.getExportStatus(item.export_to_ena.status, 'ena_export');
              console.log(enaExportStatus);
              this.summary.ena_import[enaImportStatus] += 1;
              this.summary.pipeline_analysis[pipelineAnalysisStatus] += 1;
              this.summary.ena_export[enaExportStatus] += 1;
            }
          } catch (err) {
            _iterator.e(err);
          } finally {
            _iterator.f();
          }
        }
      }, {
        key: "getDate",
        value: function getDate(item) {
          return item.split('-')[0];
        }
      }, {
        key: "getExportStatus",
        value: function getExportStatus(item, statusType) {
          if (item.indexOf(this.statuses[statusType].success) !== -1) {
            return 'Success';
          } else if (item.indexOf(this.statuses[statusType].started) !== -1) {
            if (this.getAllIndices(item, this.statuses[statusType].started).length >= 6) {
              return 'Failed';
            }

            return 'Processing';
          } else {
            return 'Undefined';
          }
        }
      }, {
        key: "getAllIndices",
        value: function getAllIndices(arr, val) {
          var indices = [];
          var i = -1;

          while (arr.indexOf(val, i + 1) !== -1) {
            i = arr.indexOf(val, i + 1);
            indices.push(i);
          }

          return indices;
        }
      }, {
        key: "getExportStatusClass",
        value: function getExportStatusClass(item, statusType) {
          if (item.indexOf(this.statuses[statusType].success) !== -1) {
            return 'badge badge-pill badge-success';
          } else if (item.indexOf(this.statuses[statusType].started) !== -1) {
            if (this.getAllIndices(item, this.statuses[statusType].started).length >= 6) {
              return 'badge badge-pill badge-danger';
            }

            return 'badge badge-pill badge-warning';
          } else {
            return 'badge badge-pill badge-info';
          }
        }
      }]);

      return OntSamplesComponent;
    }();

    OntSamplesComponent.ctorParameters = function () {
      return [{
        type: _angular_platform_browser__WEBPACK_IMPORTED_MODULE_2__["Title"]
      }, {
        type: _services_api_data_service__WEBPACK_IMPORTED_MODULE_3__["ApiDataService"]
      }];
    };

    OntSamplesComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
      selector: 'app-ont-samples',
      template: tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! raw-loader!./ont-samples.component.html */
      "./node_modules/raw-loader/dist/cjs.js!./src/app/ont-samples/ont-samples.component.html"))["default"],
      styles: [tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! ./ont-samples.component.css */
      "./src/app/ont-samples/ont-samples.component.css"))["default"]]
    })], OntSamplesComponent);
    /***/
  },

  /***/
  "./src/app/samples-details/samples-details.component.css":
  /*!***************************************************************!*\
    !*** ./src/app/samples-details/samples-details.component.css ***!
    \***************************************************************/

  /*! exports provided: default */

  /***/
  function srcAppSamplesDetailsSamplesDetailsComponentCss(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = ".row {\n  margin-bottom: 25px;\n}\n\na {\n  text-decoration: none;\n  color: white;\n}\n\nli {\n  margin-top: 5px;\n}\n\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvc2FtcGxlcy1kZXRhaWxzL3NhbXBsZXMtZGV0YWlscy5jb21wb25lbnQuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBO0VBQ0UsbUJBQW1CO0FBQ3JCOztBQUVBO0VBQ0UscUJBQXFCO0VBQ3JCLFlBQVk7QUFDZDs7QUFFQTtFQUNFLGVBQWU7QUFDakIiLCJmaWxlIjoic3JjL2FwcC9zYW1wbGVzLWRldGFpbHMvc2FtcGxlcy1kZXRhaWxzLmNvbXBvbmVudC5jc3MiLCJzb3VyY2VzQ29udGVudCI6WyIucm93IHtcbiAgbWFyZ2luLWJvdHRvbTogMjVweDtcbn1cblxuYSB7XG4gIHRleHQtZGVjb3JhdGlvbjogbm9uZTtcbiAgY29sb3I6IHdoaXRlO1xufVxuXG5saSB7XG4gIG1hcmdpbi10b3A6IDVweDtcbn1cbiJdfQ== */";
    /***/
  },

  /***/
  "./src/app/samples-details/samples-details.component.ts":
  /*!**************************************************************!*\
    !*** ./src/app/samples-details/samples-details.component.ts ***!
    \**************************************************************/

  /*! exports provided: SamplesDetailsComponent */

  /***/
  function srcAppSamplesDetailsSamplesDetailsComponentTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "SamplesDetailsComponent", function () {
      return SamplesDetailsComponent;
    });
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js");
    /* harmony import */


    var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
    /*! @angular/core */
    "./node_modules/@angular/core/fesm2015/core.js");
    /* harmony import */


    var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(
    /*! @angular/router */
    "./node_modules/@angular/router/fesm2015/router.js");
    /* harmony import */


    var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(
    /*! @angular/platform-browser */
    "./node_modules/@angular/platform-browser/fesm2015/platform-browser.js");
    /* harmony import */


    var _services_api_data_service__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(
    /*! @services/api-data.service */
    "./src/app/services/api-data.service.ts");

    var SamplesDetailsComponent = /*#__PURE__*/function () {
      function SamplesDetailsComponent(route, title, dataService) {
        _classCallCheck(this, SamplesDetailsComponent);

        this.route = route;
        this.title = title;
        this.dataService = dataService;
      }

      _createClass(SamplesDetailsComponent, [{
        key: "ngOnInit",
        value: function ngOnInit() {
          var _this4 = this;

          this.title.setTitle('Sample Logs details');
          this.route.params.subscribe(function (params) {
            _this4.sampleId = params.id;

            _this4.dataService.getSampleJovian(_this4.sampleId).subscribe(function (data) {
              _this4.data = data.results;
            }, function (error) {
              console.log(error);
            });
          });
        }
      }]);

      return SamplesDetailsComponent;
    }();

    SamplesDetailsComponent.ctorParameters = function () {
      return [{
        type: _angular_router__WEBPACK_IMPORTED_MODULE_2__["ActivatedRoute"]
      }, {
        type: _angular_platform_browser__WEBPACK_IMPORTED_MODULE_3__["Title"]
      }, {
        type: _services_api_data_service__WEBPACK_IMPORTED_MODULE_4__["ApiDataService"]
      }];
    };

    SamplesDetailsComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
      selector: 'app-samples-details',
      template: tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! raw-loader!./samples-details.component.html */
      "./node_modules/raw-loader/dist/cjs.js!./src/app/samples-details/samples-details.component.html"))["default"],
      styles: [tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! ./samples-details.component.css */
      "./src/app/samples-details/samples-details.component.css"))["default"]]
    })], SamplesDetailsComponent);
    /***/
  },

  /***/
  "./src/app/samples/samples.component.css":
  /*!***********************************************!*\
    !*** ./src/app/samples/samples.component.css ***!
    \***********************************************/

  /*! exports provided: default */

  /***/
  function srcAppSamplesSamplesComponentCss(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony default export */


    __webpack_exports__["default"] = "button {\n  margin-left: 5px;\n}\n\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvc2FtcGxlcy9zYW1wbGVzLmNvbXBvbmVudC5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7RUFDRSxnQkFBZ0I7QUFDbEIiLCJmaWxlIjoic3JjL2FwcC9zYW1wbGVzL3NhbXBsZXMuY29tcG9uZW50LmNzcyIsInNvdXJjZXNDb250ZW50IjpbImJ1dHRvbiB7XG4gIG1hcmdpbi1sZWZ0OiA1cHg7XG59XG4iXX0= */";
    /***/
  },

  /***/
  "./src/app/samples/samples.component.ts":
  /*!**********************************************!*\
    !*** ./src/app/samples/samples.component.ts ***!
    \**********************************************/

  /*! exports provided: SamplesComponent */

  /***/
  function srcAppSamplesSamplesComponentTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "SamplesComponent", function () {
      return SamplesComponent;
    });
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js");
    /* harmony import */


    var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
    /*! @angular/core */
    "./node_modules/@angular/core/fesm2015/core.js");
    /* harmony import */


    var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(
    /*! @angular/platform-browser */
    "./node_modules/@angular/platform-browser/fesm2015/platform-browser.js");
    /* harmony import */


    var _services_api_data_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(
    /*! @services/api-data.service */
    "./src/app/services/api-data.service.ts");

    var SamplesComponent = /*#__PURE__*/function () {
      function SamplesComponent(title, dataService) {
        _classCallCheck(this, SamplesComponent);

        this.title = title;
        this.dataService = dataService;
        this.p = 1;
        this.statuses = {
          ena_import: {
            success: 'download finished',
            failed: 'download failed'
          },
          pipeline_analysis: {
            success: 'pipeline finished',
            failed: 'pipeline finished with errors'
          },
          ena_export: {
            success: 'submission to ENA finished',
            failed: 'submission to ENA failed'
          }
        };
      }

      _createClass(SamplesComponent, [{
        key: "ngOnInit",
        value: function ngOnInit() {
          var _this5 = this;

          this.title.setTitle('Samples Logs');
          this.dataService.getMockJovianSamples().subscribe(function (data) {
            _this5.data = data.results;
          }, function (error) {
            console.log(error);
          });
        }
      }, {
        key: "getDate",
        value: function getDate(item) {
          return item.split('-')[0];
        }
      }, {
        key: "getExportStatus",
        value: function getExportStatus(item, statusType) {
          if (item.indexOf(this.statuses[statusType].success) !== -1) {
            return 'Success';
          } else if (item.indexOf(this.statuses[statusType].failed) !== -1) {
            return 'Failed';
          } else {
            return 'Undefined';
          }
        }
      }, {
        key: "getExportStatusClass",
        value: function getExportStatusClass(item, statusType) {
          if (item.indexOf(this.statuses[statusType].success) !== -1) {
            return 'badge badge-pill badge-success';
          } else if (item.indexOf(this.statuses[statusType].failed) !== -1) {
            return 'badge badge-pill badge-danger';
          } else {
            return 'badge badge-pill badge-info';
          }
        }
      }]);

      return SamplesComponent;
    }();

    SamplesComponent.ctorParameters = function () {
      return [{
        type: _angular_platform_browser__WEBPACK_IMPORTED_MODULE_2__["Title"]
      }, {
        type: _services_api_data_service__WEBPACK_IMPORTED_MODULE_3__["ApiDataService"]
      }];
    };

    SamplesComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
      selector: 'app-samples',
      template: tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! raw-loader!./samples.component.html */
      "./node_modules/raw-loader/dist/cjs.js!./src/app/samples/samples.component.html"))["default"],
      styles: [tslib__WEBPACK_IMPORTED_MODULE_0__["__importDefault"](__webpack_require__(
      /*! ./samples.component.css */
      "./src/app/samples/samples.component.css"))["default"]]
    })], SamplesComponent);
    /***/
  },

  /***/
  "./src/app/services/api-data.service.ts":
  /*!**********************************************!*\
    !*** ./src/app/services/api-data.service.ts ***!
    \**********************************************/

  /*! exports provided: ApiDataService */

  /***/
  function srcAppServicesApiDataServiceTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "ApiDataService", function () {
      return ApiDataService;
    });
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js");
    /* harmony import */


    var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
    /*! @angular/core */
    "./node_modules/@angular/core/fesm2015/core.js");
    /* harmony import */


    var _angular_common_http__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(
    /*! @angular/common/http */
    "./node_modules/@angular/common/fesm2015/http.js");
    /* harmony import */


    var rxjs__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(
    /*! rxjs */
    "./node_modules/rxjs/_esm2015/index.js");
    /* harmony import */


    var rxjs_operators__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(
    /*! rxjs/operators */
    "./node_modules/rxjs/_esm2015/operators/index.js");
    /* harmony import */


    var _services_api_url__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(
    /*! @services/api-url */
    "./src/app/services/api-url.ts");
    /* harmony import */


    var _jovian_mock_json__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(
    /*! ./jovian-mock.json */
    "./src/app/services/jovian-mock.json");

    var _jovian_mock_json__WEBPACK_IMPORTED_MODULE_6___namespace = /*#__PURE__*/__webpack_require__.t(
    /*! ./jovian-mock.json */
    "./src/app/services/jovian-mock.json", 1);

    var ApiDataService = /*#__PURE__*/function () {
      function ApiDataService(http) {
        _classCallCheck(this, ApiDataService);

        this.http = http;
      }

      _createClass(ApiDataService, [{
        key: "getAllSamplesJovian",
        value: function getAllSamplesJovian() {
          return this.http.get(Object(_services_api_url__WEBPACK_IMPORTED_MODULE_5__["apiUrl"])('jovian')).pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_4__["retry"])(3), Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_4__["catchError"])(this.handleError));
        }
      }, {
        key: "getMockJovianSamples",
        value: function getMockJovianSamples() {
          return Object(rxjs__WEBPACK_IMPORTED_MODULE_3__["of"])(_jovian_mock_json__WEBPACK_IMPORTED_MODULE_6__);
        }
      }, {
        key: "getSampleJovian",
        value: function getSampleJovian(id) {
          return this.http.get(Object(_services_api_url__WEBPACK_IMPORTED_MODULE_5__["apiUrl"])('jovian', id)).pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_4__["retry"])(3), Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_4__["catchError"])(this.handleError));
        }
      }, {
        key: "getAllSamplesONT",
        value: function getAllSamplesONT() {
          return this.http.get(Object(_services_api_url__WEBPACK_IMPORTED_MODULE_5__["apiUrl"])('ont')).pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_4__["retry"])(3), Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_4__["catchError"])(this.handleError));
        }
      }, {
        key: "getFilteredSamplesONT",
        value: function getFilteredSamplesONT(stage, status) {
          return this.http.get(Object(_services_api_url__WEBPACK_IMPORTED_MODULE_5__["apiUrl"])('ont', stage, status)).pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_4__["retry"])(3), Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_4__["catchError"])(this.handleError));
        }
      }, {
        key: "getSampleONT",
        value: function getSampleONT(id) {
          return this.http.get(Object(_services_api_url__WEBPACK_IMPORTED_MODULE_5__["apiUrl"])('ont', id)).pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_4__["retry"])(3), Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_4__["catchError"])(this.handleError));
        }
      }, {
        key: "handleError",
        value: function handleError(error) {
          if (error.error instanceof ErrorEvent) {
            // A client-side or network errorSubject occurred. Handle it accordingly.
            console.error('An errorSubject occurred:', error.error.message);
          } else {
            // The backend returned an unsuccessful response code.
            // The response body may contain clues as to what went wrong,
            console.error("Backend returned code ".concat(error.status, ", ") + "body was: ".concat(error.error));
            console.error(error);
          } // return an observable with a user-facing errorSubject message


          return Object(rxjs__WEBPACK_IMPORTED_MODULE_3__["throwError"])('Something bad happened; please try again later.');
        }
      }]);

      return ApiDataService;
    }();

    ApiDataService.ctorParameters = function () {
      return [{
        type: _angular_common_http__WEBPACK_IMPORTED_MODULE_2__["HttpClient"]
      }];
    };

    ApiDataService = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Injectable"])({
      providedIn: 'root'
    })], ApiDataService);
    /***/
  },

  /***/
  "./src/app/services/api-url.ts":
  /*!*************************************!*\
    !*** ./src/app/services/api-url.ts ***!
    \*************************************/

  /*! exports provided: apiUrl */

  /***/
  function srcAppServicesApiUrlTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "apiUrl", function () {
      return apiUrl;
    });
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js");

    var apiUrl = function apiUrl() {
      var protocol = 'http://';
      var domain = '193.62.54.246';

      for (var _len = arguments.length, paths = new Array(_len), _key = 0; _key < _len; _key++) {
        paths[_key] = arguments[_key];
      }

      return protocol + domain + '/api/' + paths.join('/');
    };
    /***/

  },

  /***/
  "./src/app/services/jovian-mock.json":
  /*!*******************************************!*\
    !*** ./src/app/services/jovian-mock.json ***!
    \*******************************************/

  /*! exports provided: results, default */

  /***/
  function srcAppServicesJovianMockJson(module) {
    module.exports = JSON.parse("{\"results\":[{\"export_to_ena\":{\"date\":[\"14 May, 2020 - 08:38:02\",\"14 May, 2020 - 08:38:08\",\"14 May, 2020 - 08:38:09\",\"14 May, 2020 - 08:38:09\",\"14 May, 2020 - 08:39:07\",\"14 May, 2020 - 08:39:07\",\"14 May, 2020 - 08:40:05\",\"14 May, 2020 - 08:40:05\",\"14 May, 2020 - 08:41:03\",\"14 May, 2020 - 08:41:03\",\"14 May, 2020 - 08:42:00\",\"14 May, 2020 - 08:42:00\",\"14 May, 2020 - 08:42:58\",\"14 May, 2020 - 08:42:58\",\"14 May, 2020 - 08:42:58\",\"14 May, 2020 - 08:42:58\",\"14 May, 2020 - 08:42:59\"],\"errors\":[],\"status\":[\"submission to ENA started\",\"started to render notebook\",\"back-up created successfully\",\"starting to upload /output/ERR3482174/ERR3482174-1589445482_SAMEA5867184_analysis_Rivm_Jovian_all_filtered_SNPs.tsv to ENA\",\"finishing to upload /output/ERR3482174/ERR3482174-1589445482_SAMEA5867184_analysis_Rivm_Jovian_all_filtered_SNPs.tsv to ENA\",\"starting to upload /output/ERR3482174/ERR3482174-1589445482_SAMEA5867184_analysis_Rivm_Jovian_all_virusHost.tsv to ENA\",\"finishing to upload /output/ERR3482174/ERR3482174-1589445482_SAMEA5867184_analysis_Rivm_Jovian_all_virusHost.tsv to ENA\",\"starting to upload /output/ERR3482174/ERR3482174-1589445482_SAMEA5867184_analysis_Rivm_Jovian_all_taxClassified.tsv to ENA\",\"finishing to upload /output/ERR3482174/ERR3482174-1589445482_SAMEA5867184_analysis_Rivm_Jovian_all_taxClassified.tsv to ENA\",\"starting to upload /output/ERR3482174/ERR3482174-1589445482_SAMEA5867184_analysis_Rivm_Jovian_all_taxUnclassified.tsv to ENA\",\"finishing to upload /output/ERR3482174/ERR3482174-1589445482_SAMEA5867184_analysis_Rivm_Jovian_all_taxUnclassified.tsv to ENA\",\"starting to upload /output/ERR3482174/ERR3482174-1589445482_SAMEA5867184_analysis_Rivm_Jovian_results.tar.gz to ENA\",\"finishing to upload /output/ERR3482174/ERR3482174-1589445482_SAMEA5867184_analysis_Rivm_Jovian_results.tar.gz to ENA\",\"creating analysis xml\",\"creating submission xml\",\"starting to submit xml files to ENA\",\"submission to ENA finished\"]},\"id\":\"ERR3482174\",\"import_from_ena\":{\"date\":[\"13 May, 2020 - 08:39:12\",\"13 May, 2020 - 08:39:12\",\"13 May, 2020 - 08:39:19\",\"13 May, 2020 - 08:39:19\",\"13 May, 2020 - 08:39:19\"],\"errors\":[\"--2020-05-13 08:39:15--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/004/ERR3482174/ERR3482174_2.fastq.gz\\n           => ‘/raw_data/ERR3482174/ERR3482174_2.fastq.gz’\\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\\nLogging in as dcc_byard ... \\nLogin incorrect.\\n\"],\"status\":[\"run added for download\",\"download started\",\"download finished\",\"starting to submit pipeline job\",\"submitting pipeline job succeed\"]},\"pipeline_analysis\":{\"date\":[\"13 May, 2020 - 08:39:33\",\"13 May, 2020 - 08:44:01\",\"13 May, 2020 - 09:39:18\"],\"errors\":[],\"status\":[\"pipeline started\",\"pipeline started\",\"pipeline finished\"]},\"pipeline_name\":\"Jovian\",\"sample_id\":\"SAMEA5867184\",\"study_id\":\"PRJEB34029\"},{\"export_to_ena\":{\"date\":[\"14 May, 2020 - 08:31:16\",\"14 May, 2020 - 08:31:16\",\"14 May, 2020 - 08:31:23\",\"14 May, 2020 - 08:31:23\",\"14 May, 2020 - 08:32:22\",\"14 May, 2020 - 08:32:22\",\"14 May, 2020 - 08:33:20\",\"14 May, 2020 - 08:33:20\",\"14 May, 2020 - 08:34:18\",\"14 May, 2020 - 08:34:18\",\"14 May, 2020 - 08:35:16\",\"14 May, 2020 - 08:35:16\",\"14 May, 2020 - 08:36:15\",\"14 May, 2020 - 08:36:15\",\"14 May, 2020 - 08:36:15\",\"14 May, 2020 - 08:36:15\",\"14 May, 2020 - 08:36:17\"],\"errors\":[],\"status\":[\"submission to ENA started\",\"started to render notebook\",\"back-up created successfully\",\"starting to upload /output/ERR3482177/ERR3482177-1589445076_SAMEA5867197_analysis_Rivm_Jovian_all_filtered_SNPs.tsv to ENA\",\"finishing to upload /output/ERR3482177/ERR3482177-1589445076_SAMEA5867197_analysis_Rivm_Jovian_all_filtered_SNPs.tsv to ENA\",\"starting to upload /output/ERR3482177/ERR3482177-1589445076_SAMEA5867197_analysis_Rivm_Jovian_all_virusHost.tsv to ENA\",\"finishing to upload /output/ERR3482177/ERR3482177-1589445076_SAMEA5867197_analysis_Rivm_Jovian_all_virusHost.tsv to ENA\",\"starting to upload /output/ERR3482177/ERR3482177-1589445076_SAMEA5867197_analysis_Rivm_Jovian_all_taxClassified.tsv to ENA\",\"finishing to upload /output/ERR3482177/ERR3482177-1589445076_SAMEA5867197_analysis_Rivm_Jovian_all_taxClassified.tsv to ENA\",\"starting to upload /output/ERR3482177/ERR3482177-1589445076_SAMEA5867197_analysis_Rivm_Jovian_all_taxUnclassified.tsv to ENA\",\"finishing to upload /output/ERR3482177/ERR3482177-1589445076_SAMEA5867197_analysis_Rivm_Jovian_all_taxUnclassified.tsv to ENA\",\"starting to upload /output/ERR3482177/ERR3482177-1589445076_SAMEA5867197_analysis_Rivm_Jovian_results.tar.gz to ENA\",\"finishing to upload /output/ERR3482177/ERR3482177-1589445076_SAMEA5867197_analysis_Rivm_Jovian_results.tar.gz to ENA\",\"creating analysis xml\",\"creating submission xml\",\"starting to submit xml files to ENA\",\"submission to ENA finished\"]},\"id\":\"ERR3482177\",\"import_from_ena\":{\"date\":[\"13 May, 2020 - 08:39:12\",\"13 May, 2020 - 08:39:19\",\"13 May, 2020 - 08:39:54\",\"13 May, 2020 - 08:39:54\",\"13 May, 2020 - 08:39:54\"],\"errors\":[\"--2020-05-13 08:39:19--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/007/ERR3482177/ERR3482177_1.fastq.gz\\n           => ‘/raw_data/ERR3482177/ERR3482177_1.fastq.gz’\\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\\nLogging in as dcc_byard ... \\nLogin incorrect.\\n\",\"--2020-05-13 08:39:21--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/007/ERR3482177/ERR3482177_1.fastq.gz\\n           => ‘/raw_data/ERR3482177/ERR3482177_1.fastq.gz’\\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\\nLogging in as dcc_byard ... \\nLogin incorrect.\\n\",\"--2020-05-13 08:39:24--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/007/ERR3482177/ERR3482177_1.fastq.gz\\n           => ‘/raw_data/ERR3482177/ERR3482177_1.fastq.gz’\\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\\nLogging in as dcc_byard ... \\nLogin incorrect.\\n\"],\"status\":[\"run added for download\",\"download started\",\"download finished\",\"starting to submit pipeline job\",\"submitting pipeline job succeed\"]},\"pipeline_analysis\":{\"date\":[\"13 May, 2020 - 08:40:04\",\"13 May, 2020 - 14:38:30\"],\"errors\":[],\"status\":[\"pipeline started\",\"pipeline finished\"]},\"pipeline_name\":\"Jovian\",\"sample_id\":\"SAMEA5867197\",\"study_id\":\"PRJEB34030\"},{\"export_to_ena\":{\"date\":[\"14 May, 2020 - 08:44:51\",\"14 May, 2020 - 08:44:53\",\"14 May, 2020 - 08:45:00\",\"14 May, 2020 - 08:45:00\",\"14 May, 2020 - 08:45:59\",\"14 May, 2020 - 08:45:59\",\"14 May, 2020 - 08:46:56\",\"14 May, 2020 - 08:46:56\",\"14 May, 2020 - 08:47:55\",\"14 May, 2020 - 08:47:55\",\"14 May, 2020 - 08:48:53\",\"14 May, 2020 - 08:48:53\",\"14 May, 2020 - 08:49:51\",\"14 May, 2020 - 08:49:51\",\"14 May, 2020 - 08:49:51\",\"14 May, 2020 - 08:49:51\",\"14 May, 2020 - 08:49:52\"],\"errors\":[],\"status\":[\"submission to ENA started\",\"started to render notebook\",\"back-up created successfully\",\"starting to upload /output/ERR3482180/ERR3482180-1589445891_SAMEA5867200_analysis_Rivm_Jovian_all_filtered_SNPs.tsv to ENA\",\"finishing to upload /output/ERR3482180/ERR3482180-1589445891_SAMEA5867200_analysis_Rivm_Jovian_all_filtered_SNPs.tsv to ENA\",\"starting to upload /output/ERR3482180/ERR3482180-1589445891_SAMEA5867200_analysis_Rivm_Jovian_all_virusHost.tsv to ENA\",\"finishing to upload /output/ERR3482180/ERR3482180-1589445891_SAMEA5867200_analysis_Rivm_Jovian_all_virusHost.tsv to ENA\",\"starting to upload /output/ERR3482180/ERR3482180-1589445891_SAMEA5867200_analysis_Rivm_Jovian_all_taxClassified.tsv to ENA\",\"finishing to upload /output/ERR3482180/ERR3482180-1589445891_SAMEA5867200_analysis_Rivm_Jovian_all_taxClassified.tsv to ENA\",\"starting to upload /output/ERR3482180/ERR3482180-1589445891_SAMEA5867200_analysis_Rivm_Jovian_all_taxUnclassified.tsv to ENA\",\"finishing to upload /output/ERR3482180/ERR3482180-1589445891_SAMEA5867200_analysis_Rivm_Jovian_all_taxUnclassified.tsv to ENA\",\"starting to upload /output/ERR3482180/ERR3482180-1589445891_SAMEA5867200_analysis_Rivm_Jovian_results.tar.gz to ENA\",\"finishing to upload /output/ERR3482180/ERR3482180-1589445891_SAMEA5867200_analysis_Rivm_Jovian_results.tar.gz to ENA\",\"creating analysis xml\",\"creating submission xml\",\"starting to submit xml files to ENA\",\"submission to ENA finished\"]},\"id\":\"ERR3482180\",\"import_from_ena\":{\"date\":[\"13 May, 2020 - 08:39:12\",\"13 May, 2020 - 08:39:54\",\"13 May, 2020 - 08:40:53\",\"13 May, 2020 - 08:40:53\",\"13 May, 2020 - 08:40:53\"],\"errors\":[\"--2020-05-13 08:39:54--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/000/ERR3482180/ERR3482180_1.fastq.gz\\n           => ‘/raw_data/ERR3482180/ERR3482180_1.fastq.gz’\\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\\nLogging in as dcc_byard ... \\nLogin incorrect.\\n\",\"--2020-05-13 08:40:23--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/000/ERR3482180/ERR3482180_2.fastq.gz\\n           => ‘/raw_data/ERR3482180/ERR3482180_2.fastq.gz’\\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\\nLogging in as dcc_byard ... \\nLogin incorrect.\\n\"],\"status\":[\"run added for download\",\"download started\",\"download finished\",\"starting to submit pipeline job\",\"submitting pipeline job succeed\"]},\"pipeline_analysis\":{\"date\":[\"13 May, 2020 - 08:41:03\",\"13 May, 2020 - 15:01:57\"],\"errors\":[],\"status\":[\"pipeline started\",\"pipeline finished\"]},\"pipeline_name\":\"Jovian\",\"sample_id\":\"SAMEA5867200\",\"study_id\":\"PRJEB34031\"},{\"export_to_ena\":{\"date\":[\"14 May, 2020 - 08:50:56\",\"14 May, 2020 - 08:50:57\",\"14 May, 2020 - 08:51:04\",\"14 May, 2020 - 08:51:04\",\"14 May, 2020 - 08:52:01\",\"14 May, 2020 - 08:52:01\",\"14 May, 2020 - 08:52:59\",\"14 May, 2020 - 08:52:59\",\"14 May, 2020 - 08:53:58\",\"14 May, 2020 - 08:53:58\",\"14 May, 2020 - 08:54:57\",\"14 May, 2020 - 08:54:57\",\"14 May, 2020 - 08:55:55\",\"14 May, 2020 - 08:55:55\",\"14 May, 2020 - 08:55:55\",\"14 May, 2020 - 08:55:55\",\"14 May, 2020 - 08:55:57\"],\"errors\":[],\"status\":[\"submission to ENA started\",\"started to render notebook\",\"back-up created successfully\",\"starting to upload /output/ERR3482181/ERR3482181-1589446256_SAMEA5867201_analysis_Rivm_Jovian_all_filtered_SNPs.tsv to ENA\",\"finishing to upload /output/ERR3482181/ERR3482181-1589446256_SAMEA5867201_analysis_Rivm_Jovian_all_filtered_SNPs.tsv to ENA\",\"starting to upload /output/ERR3482181/ERR3482181-1589446256_SAMEA5867201_analysis_Rivm_Jovian_all_virusHost.tsv to ENA\",\"finishing to upload /output/ERR3482181/ERR3482181-1589446256_SAMEA5867201_analysis_Rivm_Jovian_all_virusHost.tsv to ENA\",\"starting to upload /output/ERR3482181/ERR3482181-1589446256_SAMEA5867201_analysis_Rivm_Jovian_all_taxClassified.tsv to ENA\",\"finishing to upload /output/ERR3482181/ERR3482181-1589446256_SAMEA5867201_analysis_Rivm_Jovian_all_taxClassified.tsv to ENA\",\"starting to upload /output/ERR3482181/ERR3482181-1589446256_SAMEA5867201_analysis_Rivm_Jovian_all_taxUnclassified.tsv to ENA\",\"finishing to upload /output/ERR3482181/ERR3482181-1589446256_SAMEA5867201_analysis_Rivm_Jovian_all_taxUnclassified.tsv to ENA\",\"starting to upload /output/ERR3482181/ERR3482181-1589446256_SAMEA5867201_analysis_Rivm_Jovian_results.tar.gz to ENA\",\"finishing to upload /output/ERR3482181/ERR3482181-1589446256_SAMEA5867201_analysis_Rivm_Jovian_results.tar.gz to ENA\",\"creating analysis xml\",\"creating submission xml\",\"starting to submit xml files to ENA\",\"submission to ENA finished\"]},\"id\":\"ERR3482181\",\"import_from_ena\":{\"date\":[\"13 May, 2020 - 08:39:12\",\"13 May, 2020 - 08:40:53\",\"13 May, 2020 - 08:41:01\",\"13 May, 2020 - 08:41:01\",\"13 May, 2020 - 08:41:01\"],\"errors\":[\"--2020-05-13 08:40:53--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/001/ERR3482181/ERR3482181_1.fastq.gz\\n           => ‘/raw_data/ERR3482181/ERR3482181_1.fastq.gz’\\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\\nLogging in as dcc_byard ... \\nLogin incorrect.\\n\",\"--2020-05-13 08:40:56--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/001/ERR3482181/ERR3482181_1.fastq.gz\\n           => ‘/raw_data/ERR3482181/ERR3482181_1.fastq.gz’\\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\\nLogging in as dcc_byard ... \\nLogin incorrect.\\n\"],\"status\":[\"run added for download\",\"download started\",\"download finished\",\"starting to submit pipeline job\",\"submitting pipeline job succeed\"]},\"pipeline_analysis\":{\"date\":[\"13 May, 2020 - 08:41:20\",\"13 May, 2020 - 09:46:18\"],\"errors\":[],\"status\":[\"pipeline started\",\"pipeline finished\"]},\"pipeline_name\":\"Jovian\",\"sample_id\":\"SAMEA5867201\",\"study_id\":\"PRJEB34031\"},{\"export_to_ena\":{\"date\":[\"14 May, 2020 - 08:56:11\",\"14 May, 2020 - 08:56:11\",\"14 May, 2020 - 08:56:17\",\"14 May, 2020 - 08:56:17\",\"14 May, 2020 - 08:57:16\",\"14 May, 2020 - 08:57:16\",\"14 May, 2020 - 08:58:14\",\"14 May, 2020 - 08:58:14\",\"14 May, 2020 - 08:59:12\",\"14 May, 2020 - 08:59:12\",\"14 May, 2020 - 09:00:10\",\"14 May, 2020 - 09:00:10\",\"14 May, 2020 - 09:01:10\",\"14 May, 2020 - 09:01:10\",\"14 May, 2020 - 09:01:10\",\"14 May, 2020 - 09:01:10\",\"14 May, 2020 - 09:01:11\"],\"errors\":[],\"status\":[\"submission to ENA started\",\"started to render notebook\",\"back-up created successfully\",\"starting to upload /output/ERR3482182/ERR3482182-1589446571_SAMEA5867202_analysis_Rivm_Jovian_all_filtered_SNPs.tsv to ENA\",\"finishing to upload /output/ERR3482182/ERR3482182-1589446571_SAMEA5867202_analysis_Rivm_Jovian_all_filtered_SNPs.tsv to ENA\",\"starting to upload /output/ERR3482182/ERR3482182-1589446571_SAMEA5867202_analysis_Rivm_Jovian_all_virusHost.tsv to ENA\",\"finishing to upload /output/ERR3482182/ERR3482182-1589446571_SAMEA5867202_analysis_Rivm_Jovian_all_virusHost.tsv to ENA\",\"starting to upload /output/ERR3482182/ERR3482182-1589446571_SAMEA5867202_analysis_Rivm_Jovian_all_taxClassified.tsv to ENA\",\"finishing to upload /output/ERR3482182/ERR3482182-1589446571_SAMEA5867202_analysis_Rivm_Jovian_all_taxClassified.tsv to ENA\",\"starting to upload /output/ERR3482182/ERR3482182-1589446571_SAMEA5867202_analysis_Rivm_Jovian_all_taxUnclassified.tsv to ENA\",\"finishing to upload /output/ERR3482182/ERR3482182-1589446571_SAMEA5867202_analysis_Rivm_Jovian_all_taxUnclassified.tsv to ENA\",\"starting to upload /output/ERR3482182/ERR3482182-1589446571_SAMEA5867202_analysis_Rivm_Jovian_results.tar.gz to ENA\",\"finishing to upload /output/ERR3482182/ERR3482182-1589446571_SAMEA5867202_analysis_Rivm_Jovian_results.tar.gz to ENA\",\"creating analysis xml\",\"creating submission xml\",\"starting to submit xml files to ENA\",\"submission to ENA finished\"]},\"id\":\"ERR3482182\",\"import_from_ena\":{\"date\":[\"13 May, 2020 - 08:39:12\",\"13 May, 2020 - 08:41:01\",\"13 May, 2020 - 08:41:08\",\"13 May, 2020 - 08:41:08\",\"13 May, 2020 - 08:41:08\"],\"errors\":[\"--2020-05-13 08:41:02--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/002/ERR3482182/ERR3482182_2.fastq.gz\\n           => ‘/raw_data/ERR3482182/ERR3482182_2.fastq.gz’\\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\\nLogging in as dcc_byard ... \\nLogin incorrect.\\n\",\"--2020-05-13 08:41:04--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/002/ERR3482182/ERR3482182_2.fastq.gz\\n           => ‘/raw_data/ERR3482182/ERR3482182_2.fastq.gz’\\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\\nLogging in as dcc_byard ... \\nLogin incorrect.\\n\"],\"status\":[\"run added for download\",\"download started\",\"download finished\",\"starting to submit pipeline job\",\"submitting pipeline job succeed\"]},\"pipeline_analysis\":{\"date\":[\"13 May, 2020 - 08:41:19\",\"13 May, 2020 - 09:16:20\",\"10 June, 2020 - 11:06:02\",\"10 June, 2020 - 11:32:55\"],\"errors\":[],\"status\":[\"pipeline started\",\"pipeline finished\",\"pipeline started\",\"pipeline started\"]},\"pipeline_name\":\"Jovian\",\"sample_id\":\"SAMEA5867202\",\"study_id\":\"PRJEB34031\"}]}");
    /***/
  },

  /***/
  "./src/environments/environment.ts":
  /*!*****************************************!*\
    !*** ./src/environments/environment.ts ***!
    \*****************************************/

  /*! exports provided: environment */

  /***/
  function srcEnvironmentsEnvironmentTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony export (binding) */


    __webpack_require__.d(__webpack_exports__, "environment", function () {
      return environment;
    });
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js"); // This file can be replaced during build by using the `fileReplacements` array.
    // `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
    // The list of file replacements can be found in `angular.json`.


    var environment = {
      production: false
    };
    /*
     * For easier debugging in development mode, you can import the following file
     * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
     *
     * This import should be commented out in production mode because it will have a negative impact
     * on performance if an error is thrown.
     */
    // import 'zone.js/dist/zone-error';  // Included with Angular CLI.

    /***/
  },

  /***/
  "./src/main.ts":
  /*!*********************!*\
    !*** ./src/main.ts ***!
    \*********************/

  /*! no exports provided */

  /***/
  function srcMainTs(module, __webpack_exports__, __webpack_require__) {
    "use strict";

    __webpack_require__.r(__webpack_exports__);
    /* harmony import */


    var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
    /*! tslib */
    "./node_modules/tslib/tslib.es6.js");
    /* harmony import */


    var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
    /*! @angular/core */
    "./node_modules/@angular/core/fesm2015/core.js");
    /* harmony import */


    var _angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(
    /*! @angular/platform-browser-dynamic */
    "./node_modules/@angular/platform-browser-dynamic/fesm2015/platform-browser-dynamic.js");
    /* harmony import */


    var _app_app_module__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(
    /*! ./app/app.module */
    "./src/app/app.module.ts");
    /* harmony import */


    var _environments_environment__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(
    /*! ./environments/environment */
    "./src/environments/environment.ts");

    if (_environments_environment__WEBPACK_IMPORTED_MODULE_4__["environment"].production) {
      Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["enableProdMode"])();
    }

    Object(_angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_2__["platformBrowserDynamic"])().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_3__["AppModule"])["catch"](function (err) {
      return console.error(err);
    });
    /***/
  },

  /***/
  0:
  /*!***************************!*\
    !*** multi ./src/main.ts ***!
    \***************************/

  /*! no static exports found */

  /***/
  function _(module, exports, __webpack_require__) {
    module.exports = __webpack_require__(
    /*! /Users/rthorne/repositories/covid-workflow-manager/samples-logs-front-end/src/main.ts */
    "./src/main.ts");
    /***/
  }
}, [[0, "runtime", "vendor"]]]);
//# sourceMappingURL=main-es5.js.map