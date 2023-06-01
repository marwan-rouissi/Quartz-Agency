import React from "react";

function Footer() {
  return (
    <footer class="bg-white rounded-lg shadow m-4 ">
      <div class="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between">
        <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">
          © 2023{" "}
          <a href="https://www.quartzagency.com/" class="hover:underline">
            Quartz agency
          </a>
          .Tous les droits sont réservés
        </span>
        <ul class="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0">
          <li>
            <a href="#" class="mr-4 hover:underline md:mr-6 ">
              à propos
            </a>
          </li>
          <li>
            <a href="#" class="mr-4 hover:underline md:mr-6">
              condition d'utilisation
            </a>
          </li>
          <li>
            <a href="#" class="hover:underline">
              Contact
            </a>
          </li>
        </ul>
      </div>
    </footer>
  );
}

export default Footer;
