import Link from "next/link";

export default function Footer() {
  return (
    <footer className="m-4 bg-gray-300 rounded-lg shadow ">
    <div className="w-full max-w-screen-xl p-4 mx-auto md:flex md:items-center md:justify-between">
      <span className="text-sm text-gray-500 sm:text-center dark:text-gray-400">
        © 2023{" "}
        <a href="https://www.quartzagency.com/" className="hover:underline">
          Quartz agency
        </a>
        .Tous les droits sont réservés
      </span>
      <ul className="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0">
        <li>
          <a href="#" className="mr-4 hover:underline md:mr-6 ">
            à propos
          </a>
        </li>
        <li>
          <a href="#" className="mr-4 hover:underline md:mr-6">
            condition d'utilisation
          </a>
        </li>
        <li>
          <a href="#" className="hover:underline">
            Contact
          </a>
        </li>
      </ul>
    </div>
  </footer>
  );
}
